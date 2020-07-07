from datetime import datetime
from collections import OrderedDict

from output import jsonlog
from output import hpfeeds
from output import stingar


class Output:

    def __init__(self, config):
        self.config = config
        self.json_output = None
        self.hpfeeds_output = None
        self.stingar_output = None

        if self.config.getboolean('jsonlog', 'enabled', fallback=False):
            self.json_output = jsonlog.JsonOutput(self.config)

        if self.config.getboolean('hpfeeds', 'enabled', fallback=False):
            self.hpfeeds_output = hpfeeds.HpfeedsOutput(self.config)

        if self.config.getboolean('stingar', 'enabled', fallback=False):
            self.stingar_output = stingar.StingarOutput(self.config)

    def write(self, request):
        data = self.parse_request(request)
        if self.json_output:
            self.json_output.write(data)
        if self.hpfeeds_output:
            self.hpfeeds_output.write(data)
        if self.stingar_output:
            self.stingar_output.write(data)

    def parse_request(self, request):
        hp_data = OrderedDict()
        hp_data['start_time'] = datetime.isoformat(datetime.now())
        hp_data['src_ip'] = request.environ.get('REMOTE_ADDR')
        hp_data['src_port'] = request.environ.get('REMOTE_PORT')
        hp_data['dst_ip'] = self.config.get('bighp', 'reported_ip')
        hp_data['dst_port'] = self.config.get('bighp', 'reported_port')
        hp_data['method'] = request.method
        hp_data['path'] = request.path
        hp_data['full_path'] = request.full_path
        hp_data['args'] = request.args.to_dict()
        hp_data['form_data'] = request.form.to_dict()

        hp_data['headers'] = dict()
        for k, v in request.headers.items():
            hp_data['headers'][k] = v

        return hp_data
