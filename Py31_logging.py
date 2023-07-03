import random
import logging
import sys

# require Python 3.10 and newer

# Making Python loggers output all messages to stdout in addition to log file - https://bit.ly/3NqjZpm

def possibly_exploding_code():
  'some function '
  exc = random.choice([IndexError, ValueError, TypeError, None])
  if exc is not None:
    raise exc("boom")
  return "Success"

# You could create two handlers for file and stdout and then create one logger with handlers
file_handler = logging.FileHandler(filename='Py31_logging.log')
stdout_handler = logging.StreamHandler(stream=sys.stdout)
handlers = [file_handler, stdout_handler]
# logging iniicialization
logging.basicConfig(
  # filename='Py31_logging.log',
  # stream=sys.stdout, to output only to stdout
  encoding='utf-8',
  level=logging.DEBUG,
  # format=' %(name)s :: %(levelname)-8s :: %(message)s',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  handlers = handlers,
  )
logging.debug('This message should not go to the log file')
logging.info('But this should')

# logger
logger = logging.getLogger(__name__)

try:
  logger.info('Start')
  possibly_exploding_code()
except IndexError as e:
  logger.error( 'Not enough data '+str(e))
except TypeError as e:
  logger.error( 'Wrong data '+str(e))
except ValueError as e:
  logger.error( 'Data out of bounds '+str(e))
else:
  logger.info('Success')
finally:
  logger.info ('Done.\n')
