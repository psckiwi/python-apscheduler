import time
from datetime import datetime

from core import batch_job


@batch_job
def run(*args):
    print('[{}] cron_sample_job : {}'.format(datetime.now(), args))
    time.sleep(10)
    return True
