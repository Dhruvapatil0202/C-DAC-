import logging

logging.basicConfig(filename='vasicConfig.log', level =  logging.DEBUG, format = '%(asctime)s - %(level_name)s')

logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')

# Advanced config

logger = logging.getLogger('advamcedConfig_logger')
handler = logging.FileHandler('advancedConfig.log')
formatter = logging.Formatter('%(asctime)s - %(level_name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)