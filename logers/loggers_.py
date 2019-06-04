#import yaml
import logging
import logging.config

with open('config.yaml', 'r') as f:
    conf = yaml.load(f)

logging.config.dictConfig(conf)

myapp = logging.getLogger('myapp')
myapp.info('This logger will write both to console and to the logging file, since the logger\'s name is myapp')

myapp_api = logging.getLogger('myapp.api')
myapp_api.info('This should also write to both since its a descendant of myapp')

another_logger = logging.getLogger('another_app')
another_logger.info('This instead should only appear in')