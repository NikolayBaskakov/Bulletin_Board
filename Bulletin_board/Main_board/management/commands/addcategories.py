from typing import Any
from django.core.management.base import BaseCommand
from Main_board.models import Category

class Command(BaseCommand):
    help = 'Create all of available categories in Category.TYPES '
    requires_migrations_checks = True
    
    def handle(self, *args, **options):
        for category in Category.TYPES:
            Category.objects.create(name=category[0])