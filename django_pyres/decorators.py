from django_pyres.conf import settings
from .core import pyres

def job(queue):
    def wrapper(func):
        def enqueue(*args):
            if settings.PYRES_USE_QUEUE:
                class_name = '%s.%s' % (func.__module__, func.__name__)
                pyres.enqueue_from_string(class_name, queue, *args)
            else:
                return func(*args)

        def __call__(self, *args):
            return func(*args)

        new_class = type('Job',(),{
            'queue': queue,
            'perform': staticmethod(func),
            'enqueue': staticmethod(enqueue),
            '__call__': __call__,
            '__name__': func.__name__
        })
        return new_class()
    return wrapper


