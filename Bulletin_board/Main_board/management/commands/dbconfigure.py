from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from Main_board.models import Category, User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Configure database for using'
    requires_migrations_checks = True
    
    def handle(self, *args, **options):
        try:
            for category in Category.TYPES:
                category_obj= Category.objects.create(name=category[0])
                self.stdout.write(f'Create <Category.object: {category_obj.name}> ')
            content_type = ContentType.objects.get_for_model(User)
            perm = Permission.objects.create(codename="standard", name="Standard",  content_type=content_type)
            self.stdout.write(f'Create <Permission.object: {perm}> ')
            group = Group.objects.create(name='common_users')
            self.stdout.write(f'Create <Group.object: {group}> ')
            group.permissions.add(perm)
            self.stdout.write(f'Add <Permission.object: {perm.name}> to <Group.object: {group.name}> ')
        except IntegrityError:
            self.stdout.write('Objects allready exixts. News objects haven`t been created.')
        