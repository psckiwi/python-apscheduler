from datetime import datetime

from core import batch_job


@batch_job
def run(*args):
    print('[{}] date_sample_job : {}'.format(datetime.now(), args))
    return True
