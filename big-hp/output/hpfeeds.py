import json
import hpfeeds


class HpfeedsOutput:
    """
    jsonlog output
    """

    def __init__(self, config):
        self.config = config
        self.log_get = self.config.getboolean('jsonlog', 'log_get', fallback=False)
        self.channel = "big-hp.events"
        self.server = config.get('hpfeeds', 'server')
        self.port = config.getint('hpfeeds', 'port')
        self.ident = config.get('hpfeeds', 'ident')
        self.secret = config.get('hpfeeds', 'secret')
        self.tags = config.get('hpfeeds', 'tags')
        self.client = hpfeeds.new(self.server, self.port, self.ident, self.secret)

    def write(self, data):
        if (self.log_get is False) and (data.get('method') == "GET"):
            return
        print("writing hpfeeds...")
        self.client.publish(self.channel, json.dumps(data).encode('utf-8'))
        print("hpfeeds written.")
