from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction

from ccam.core.models import get_sentinel_user
from ccam.people.models import Person
from ccam.people.seac.models import SEACStaff

User = get_user_model()


class Command(BaseCommand):
    help = "Creates default superuser, sentinel user and first manager"

    def create_sentinel_user(self):
        try:
            User.objects.create_user(username="deleted", password="abc", is_active=False)
            self.stdout.write(self.style.SUCCESS("Sentinel user created"))
        except IntegrityError:
            self.stdout.write(self.style.WARNING("Sentinel user is already created"))

    def create_seac_coordinator(self):
        sentinel = get_sentinel_user()
        profile_picture_path = Path("ccam/static/images/victor_profile_picture.jpg")

        # transaction.atomic() used in case SEACStaff creation fails, it will rollback the created Person
        with transaction.atomic():
            with profile_picture_path.open(mode="rb") as file:
                profile_picture = File(file, name=profile_picture_path.name)
                seac_person, person_created = Person.objects.get_or_create(
                    name="Vitor Cunha Alves",
                    email="vitor.c@gmail.com",
                    registration="20231874523467",
                    sex=Person.Sex.MALE,
                    cpf="236.478.630-41",
                    created_by=sentinel,
                    updated_by=sentinel,
                    defaults={
                        "profile_picture": profile_picture,
                    },
                )

            SEACStaff.objects.get_or_create(
                phone_line="(84) 4005 4109",
                role=SEACStaff.Role.COORDINATOR,
                person=seac_person,
                created_by=sentinel,
                updated_by=sentinel,
            )
            if not person_created:
                self.stdout.write(self.style.WARNING(f"SEAC Coordinator {seac_person.name} is already created"))
            else:
                self.stdout.write(self.style.SUCCESS(f"SEAC Coordinator {seac_person.name} created successfully"))

    def create_superuser(self):
        try:
            User.objects.create_user(username="admin", password="ccam.admin@PF", is_superuser=True, is_staff=True)
            self.stdout.write(self.style.SUCCESS("Superuser created"))
        except IntegrityError:
            self.stdout.write(self.style.WARNING("Superuser is already created"))

    def handle(self, *args, **kwargs):
        self.create_sentinel_user()
        self.create_seac_coordinator()
        self.create_superuser()
