# images/management/commands/createsu.py

from accounts.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """``py manage.py createsu`` Creates a superuser with defined username and password using the custom ``User`` model"""

    def handle(self, *args, **options):
        username = 'admin'
        password = 'Abcd2003@'

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(
                username=username,
            )
            user.set_password(password)
            user.save()
            print(f'Superuser with username {username} and {password} has been created.')
        else:
            print(f'Superuser with username {username} already exists.')
