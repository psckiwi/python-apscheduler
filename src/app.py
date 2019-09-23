import json
import logging
import logging.config
import os
from typing import List

from apscheduler.events import JobExecutionEvent, EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.job import Job
from apscheduler.schedulers.blocking import BlockingScheduler

from config import JOB_STORES, EXECUTORS, JOB_DEFAULTS, LOG_CONF_PATH
from jobs import add_jobs

logger = logging.getLogger('app.root')


def get_jobs():
    jobs: List[Job] = scheduler.get_jobs()
    logger.info('*' * 80)
    for job in jobs:
        logger.info(job)
    logger.info('*' * 80)


def job_listener(event: JobExecutionEvent):
    if event.exception:
        logger.error('The job crashed : {}'.format(event.job_id))
    else:
        logger.info('The job worked : {} -> {}'.format(event.job_id, event.retval))


def init():
    with open(LOG_CONF_PATH, 'r') as f:
        dict_config: dict = json.load(f)

    logging.config.dictConfig(config=dict_config)

    logging.getLogger('apscheduler').setLevel(logging.ERROR)


try:
    scheduler: BlockingScheduler = BlockingScheduler(jobstores=JOB_STORES,
                                                     executors=EXECUTORS,
                                                     job_defaults=JOB_DEFAULTS)
    init()
    add_jobs(scheduler)
    scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    get_jobs()
    scheduler.start()


except (KeyboardInterrupt, SystemExit) as e:
    logger.error('System Error : {}'.format(e))
