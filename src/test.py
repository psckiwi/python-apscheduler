from datetime import datetime

from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED, JobExecutionEvent
from apscheduler.schedulers.blocking import BlockingScheduler

cnt: int = 1


def my_job(*args):
    print('[{}] my_job stared {}'.format(datetime.now(), args))
    return True


def my_listener(event: JobExecutionEvent):
    if event.exception:
        print('The job crashed : {}'.format(event.job_id))
    else:
        print('The job worked : {} -> {}'.format(event.job_id, event.retval))


scheduler = BlockingScheduler()

scheduler.add_job(trigger='interval', max_instances=1,
                  id='my_job', func=my_job, args=['hello', 'world'],
                  seconds=1)

scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

scheduler.start()
