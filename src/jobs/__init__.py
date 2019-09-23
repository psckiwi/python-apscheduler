from jobs.cron import cron_sample_job
from jobs.date import date_sample_job
from jobs.interval import interval_sample_job
from datetime import date


# ------------------------------------------------------------------------------------------------
# kinds of trigger
# - cron: use when you want to run the job periodically at certain time(s) of day
# - interval: use when you want to run the job at fixed intervals of time
# - date: use when you want to run the job just once at a certain point of time
# - calendarinterval: use when you want to run the job on calendar-based intervals, at a specific time of day
# ------------------------------------------------------------------------------------------------
def add_jobs(scheduler):
    add_cron_jobs(scheduler)
    add_interval_jobs(scheduler)
    add_date_jobs(scheduler)


def add_cron_jobs(scheduler):
    scheduler.add_job(trigger='cron',
                      id='cron_sample_job', func=cron_sample_job.run, args=['hello', 'cron job'],
                      year='*', month='*', day='*', hour='*', minute='*', second='*/1')


def add_interval_jobs(scheduler):
    scheduler.add_job(trigger='interval',
                      id='interval_sample_job', func=interval_sample_job.run, args=['hello', 'interval job'],
                      seconds=3)


def add_date_jobs(scheduler):
    scheduler.add_job(trigger='date',
                      id='date_sample_job', func=date_sample_job.run, args=['hello', 'date job'],
                      run_date=date(2019, 9, 24))
