import logging
logging.basicConfig(level=logging.INFO)
vinod = logging.getLogger(__name__)

vinod.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
vinod.debug('Records: %s', records)
vinod.info('Updating records ...')
# update records here
vinod.info('Finish updating records')