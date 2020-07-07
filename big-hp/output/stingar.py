from fluent import sender

SPYLEX_TOPIC = 'events.big-hp'


class StingarOutput:
    """
    jsonlog output
    """

    def __init__(self, config):
        self.config = config
        fluent_host = self.config.get('stingar', 'fluent_host')
        fluent_port = self.config.getint('stingar', 'fluent_port')
        app = self.config.get('stingar', 'app')
        self.hostname = self.config.get('stingar', 'hostname')
        self.identifier = self.config.get('stingar', 'identifier')
        self.tags = self.config.get('stingar', 'tags')
        self.asn = self.config.get('stingar', 'asn')
        self.log_get = self.config.getboolean('stingar', 'log_get', fallback=False)

        self.sender = sender.FluentSender(app, host=fluent_host, port=fluent_port)

    def write(self, data):
        event = {'app': 'spylex',
                 'sensor': {
                     'uuid': self.identifier,
                     'hostname': self.hostname,
                     'tags': self.tags,
                     'asn': self.asn
                 },
                 'protocol': 'http',
                 'start_time': data.get('start_time'),
                 'end_time': '',
                 'src_ip': data.get('src_ip'),
                 'src_port': data.get('src_port'),
                 'dst_ip': data.get('dst_ip'),
                 'dst_port': data.get('dst_port'),
                 'hp_data': {
                     'method': data.get('method'),
                     'path': data.get('path'),
                     'full_path': data.get('full_path'),
                     'args': data.get('args'),
                     'form_data': data.get('form_data'),
                     'headers': data.get('headers'),
                     'files': data.get('files')}
                 }
        self.sender.emit(SPYLEX_TOPIC, event)
