from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

LOG_CONF_PATH = '../conf/logging.json'

JOB_STORES = {
    'default': MemoryJobStore()
    # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

EXECUTORS = {
    'default': ThreadPoolExecutor(10),
}

JOB_DEFAULTS = {
    'coalesce': False,
    'max_instances': 1
}
