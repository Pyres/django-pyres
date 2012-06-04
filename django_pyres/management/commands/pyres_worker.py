import logging
from django.core.management.base import BaseCommand, CommandError
from django_pyres.conf import settings

from optparse import make_option
from pyres.worker import Worker
from pyres import setup_logging, setup_pidfile

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-l', '--log-level', dest='log_level', default='info', help='log level.  Valid values are "debug", "info", "warning", "error", "critical", in decreasing order of verbosity. Defaults to "info" if parameter not specified.'),
    )
    help = 'Closes the specified poll for voting'

    def handle(self, queue_list, **options):
        queues = queue_list.split(',')
        log_level = getattr(logging, options['log_level'].upper(), 'INFO')
        setup_logging(procname="pyres_worker", log_level=log_level, filename=None)
        setup_pidfile(settings.PYRES_WORKER_PIDFILE)
        Worker.run(
            queues, 
            settings.PYRES_HOST,
            settings.PYRES_WORKER_INTERVAL, 
            timeout=settings.PYRES_WORKER_TIMEOUT
        )


