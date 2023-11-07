from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import IntegrityError

User = get_user_model()


class Command(BaseCommand):
    help = "Creates default superuser, sentinel user and first manager"

    def handle(self, *args, **kwargs):
        try:
            User.objects.create_user(username="deleted", password="abc", is_active=False)
        except IntegrityError:
            self.stdout.write(self.style.WARNING("Sentinel user is already created"))
