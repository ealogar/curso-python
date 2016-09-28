import logging
import logging.config
import yaml

with open('logger.yml') as logger_config:
    logging.config.dictConfig(yaml.safe_load(logger_config))
    
# The ```os``` module goes to syslog
syslog = logging.getLogger('os')
syslog.critical("To syslog")