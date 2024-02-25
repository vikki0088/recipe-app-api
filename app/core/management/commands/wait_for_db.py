"""

Django command to wait for database

"""
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    django commad for wait for db
    """

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write("waiting for database.....")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2Error, OperationalError):
                self.stdout.write('Database is unavailable, waiting for 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available!'))
