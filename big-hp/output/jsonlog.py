import json
import logging

logging.basicConfig(level=logging.INFO)


class JsonOutput:
    """
    jsonlog output
    """

    def __init__(self, config):
        json_fname = config.get('jsonlog', 'json_file')
        self.outfile = open(json_fname, 'a')

    def write(self, data):
        logging.info(json.dumps(data))
        self.outfile.write(json.dumps(data) + "\n")
        self.outfile.flush()
