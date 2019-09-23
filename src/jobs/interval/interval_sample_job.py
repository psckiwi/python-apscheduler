import time
from datetime import datetime

from core import batch_job


@batch_job
def run(*args):
    print('[{}] interval_sample_job : {}'.format(datetime.now(), args))
    time.sleep(1)
    return True
