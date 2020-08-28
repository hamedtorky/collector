from logging import getLogger
from django.core.management.base import BaseCommand, CommandError

from Collector.models import Connection as conn



__author__ = 'HamedTorky'
__name__ = 'pipline thread'
logger = getLogger(__name__)

class Command(BaseCommand):
    help = 'Pipline'

    def add_arguments(self, parser):
        parser.add_argument('method', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            
        except Exception as err:
            print (err)