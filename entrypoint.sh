#!/bin/bash

trap "exit 130" SIGINT
trap "exit 137" SIGKILL
trap "exit 143" SIGTERM

set -o errexit
set -o nounset
set -o pipefail


main () {

    DEBUG=${DEBUG:-false}
    if [[ ${DEBUG} == "true" ]]
    then
      set -o xtrace
      BIGHP_DEBUG="-v"
    else
      BIGHP_DEBUG=""
    fi

    # Register this host with CHN if needed
    chn-register.py \
        -p big-hp \
        -d "${DEPLOY_KEY}" \
        -u "${CHN_SERVER}" -k \
        -o "${BIGHP_JSON}" \
        -i "${IP_ADDRESS}"

    local uid="$(cat ${BIGHP_JSON} | jq -r .identifier)"
    local secret="$(cat ${BIGHP_JSON} | jq -r .secret)"

    # Keep old var names, but create also create some new ones that
    # containedenv can understand

    export BIGHP_bighp__ip_address="${IP_ADDRESS}"
    export BIGHP_bighp__reported_ip="${REPORTED_IP}"
    export BIGHP_bighp__reported_port="${REPORTED_PORT}"
    export BIGHP_bighp__hostname="${HOSTNAME}"
    export BIGHP_hpfeeds__enabled="True"
    export BIGHP_hpfeeds__server="${FEEDS_SERVER}"
    export BIGHP_hpfeeds__port="${FEEDS_SERVER_PORT:-10000}"
    export BIGHP_hpfeeds__ident="${uid}"
    export BIGHP_hpfeeds__secret="${secret}"
    export BIGHP_hpfeeds__tags="${TAGS}"

    # Write out custom conpot config
    containedenv-config-writer.py \
      -p BIGHP_ \
      -f ini \
      -r /opt/big-hp/conf/big-hp.cfg.template \
      -o /opt/big-hp/big-hp.cfg

    cd /opt/big-hp/big-hp
    gunicorn --certfile /opt/big-hp/cert.pem --keyfile /opt/big-hp/key.pem --access-logfile - -b 0.0.0.0:8000 -k gevent app
}

main "$@"
