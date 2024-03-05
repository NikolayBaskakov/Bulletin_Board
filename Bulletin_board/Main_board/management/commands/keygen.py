from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(f'Your secret key: {get_random_secret_key()}')