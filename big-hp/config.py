import socket
import logging
from configparser import ConfigParser


def parse_config(config_file):
    bighp_config = ConfigParser()

    try:
        bighp_config.read(config_file)
    except AttributeError as e:
        print(e)
        logging.error("Can't find config file: %s", config_file)

    if not bighp_config.get("bighp", "ip_address"):
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        bighp_config.set("bighp", "ip_address", host_ip)

    if not bighp_config.getint("bighp", "reported_port"):
        bighp_config.set("bighp", "reported_port", 80)

    return bighp_config
