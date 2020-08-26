from logging import getLogger
from django.core.management.base import BaseCommand, CommandError


__author__ = 'HamedTorky'
logger = getLogger(__name__)

class Command(BaseCommand):
    help = 'Data collector '

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        try:
            print("Hello .... \n")
        except expression as identifier:
            pass