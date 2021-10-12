import logging

import logstash

host = 'localhost'

test_logger = logging.getLogger ( 'python-logstash-logger' )
test_logger.setLevel ( logging.INFO )
test_logger.addHandler ( logstash.LogstashHandler ( host, 5959, version=1 ) )
