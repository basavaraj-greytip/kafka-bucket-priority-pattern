import os

BOOTSTRAP_SERVERS = os.environ['BOOTSTRAP_SERVERS'].split(',')
TOPIC_NAME = os.environ['TOPIC_NAME']

WORKERS_NUM = int(os.environ.get('WORKERS_NUM', 1))
RUN_SECONDS = int(os.environ.get('RUN_SECONDS', 30))

CONSUMER_MIN_SLEEP_TIME = float(os.environ.get('CONSUMER_MIN_SLEEP_TIME', 0.025))
CONSUMER_MAX_SLEEP_TIME = float(os.environ.get('CONSUMER_MAX_SLEEP_TIME', 0.075))
