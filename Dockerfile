FROM python:alpine3.7

ENV CONFIG "/opt/big-hp/big-hp.cfg"
ENV BIGHP_JSON "/etc/big-hp/big-hp.json"

# hadolint ignore=DL3018
RUN apk add --no-cache git python3-dev libffi-dev gcc musl-dev make openssl bash jq

WORKDIR /opt
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN git clone --depth=1 https://github.com/communityhoneynetwork/big-hp.git
WORKDIR /opt/big-hp
RUN pip install -r requirements.txt

COPY entrypoint.sh /opt/big-hp
RUN chmod 0755 /opt/big-hp/entrypoint.sh

RUN openssl req -subj '/CN=localhost' -x509 -newkey rsa:4096 -nodes -keyout key.pem -out cert.pem -days 365

ENTRYPOINT ["/opt/big-hp/entrypoint.sh"]
