import logging
import json


list_of_log = [
    {'name': 'test_01', 'file_name': 'test_01.log', 'Stream': True},
    {'name': 'test_02', 'file_name': 'test_02.log'}
    ]


class LogConfigActivator:
    default_config = {'stream_name': 'name', 'file_name': 'default_file.log', 'stream': False,
                      'stream_min_level': logging.INFO, 'file_s': True, 'file_min_level': logging.INFO}
    log_file_path = '/var/log/'  # path for dir with log file

    long_format = '%(levelname)s - %(asctime)s - %(message)s'
    date_format_long = '%d-%b-%y %H:%M:%S'
    shot_format = '%(levelname)s - %(message)s'

    def setup_logger(self, in_config):
        config = self.default_config | in_config

        logger = logging.getLogger(config['stream_name'])
        logger.setLevel(logging.INFO)

        if config['file_s'] is True:
            f_handler = logging.FileHandler(f"{self.log_file_path}{config['file_name']}", mode='a')
            f_handler.setLevel(config['file_min_level'])
            f_format = logging.Formatter(self.long_format, datefmt=self.date_format_long)
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)

        if config['stream'] is True:
            c_handler = logging.StreamHandler()
            c_handler.setLevel(config['stream_min_level'])
            c_format = logging.Formatter(self.shot_format)
            c_handler.setFormatter(c_format)
            logger.addHandler(c_handler)

    def __init__(self):
        for log_conf in list_of_log:
            self.setup_logger(log_conf)


