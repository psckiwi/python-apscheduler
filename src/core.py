from logging import getLogger

logger = getLogger('app.core')


def batch_job(original_fn):
    def wrapper_fn(*args, **kwargs):
        logger.info('-' * 79)
        logger.info('{}.{} started : {}'.format(original_fn.__module__, original_fn.__name__, args))
        logger.info('-' * 79)
        return original_fn(*args, **kwargs)

    return wrapper_fn
