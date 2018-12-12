import logging


# logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level=logging.DEBUG,
    filename='logs.txt'
)

# logger = logging.getLogger('test_logger')
logger = logging.getLogger(__name__)

logger.debug('Debug')
logger.info('This will not show up.')
logger.warning('This will.')
logger.error('Error')
logger.critical('Critical Error')
logger.debug('This is a debug message.')
logger.critical('A critical error occurred.')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""