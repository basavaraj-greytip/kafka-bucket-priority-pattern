import os

BOOTSTRAP_SERVERS = os.environ['BOOTSTRAP_SERVERS'].split(',')
TOPIC_NAME = os.environ['TOPIC_NAME']

WORKERS_NUM = int(os.environ.get('WORKERS_NUM', 1))
RUN_SECONDS = int(os.environ.get('RUN_SECONDS', 5))

CREATOR_MIN_SLEEP_TIME = float(os.environ.get('CREATOR_MIN_SLEEP_TIME', 0.001))
CREATOR_MAX_SLEEP_TIME = float(os.environ.get('CREATOR_MAX_SLEEP_TIME', 0.005))
