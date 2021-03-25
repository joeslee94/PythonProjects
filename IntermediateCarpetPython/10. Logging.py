import logging
logger = logging.getLogger(__name__)
# create handler
streamHandler = logging.StreamHandler()
fileHandler = logging.FileHandler('file.log')

#level and format of the handler
streamHandler.setLevel(logging.WARNING)
fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

logger.warning('This is a warning')
logger.warning('This is an error')

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%H:%S')
#
# import LoggingHelper

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")