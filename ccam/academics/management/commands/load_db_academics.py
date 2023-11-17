from django.core.management.base import BaseCommand

from ccam.academics.models import Course
from ccam.core.models import get_sentinel_user


class Command(BaseCommand):
    help = "Loads courses to database"

    def log_course_creation_feedback(self, course_name, created):
        if created:
            self.stdout.write(self.style.SUCCESS(f"{course_name} course created"))
        else:
            self.stdout.write(self.style.WARNING(f"{course_name} course already created"))

    def handle(self, *args, **options):
        sentinel_user = get_sentinel_user()
        ads_course, ads_created = Course.objects.get_or_create(
            name="Tecnólogo em Análise e Desenvolvimento de Sistemas - ADS",
            duration=7,
            created_by=sentinel_user,
            updated_by=sentinel_user,
        )
        agro_course, agro_created = Course.objects.get_or_create(
            name="Tecnólogo Agroindústria", duration=7, created_by=sentinel_user, updated_by=sentinel_user
        )
        chem_course, chem_created = Course.objects.get_or_create(
            name="Licenciatura Química", duration=8, created_by=sentinel_user, updated_by=sentinel_user
        )
        it_course, it_created = Course.objects.get_or_create(
            name="Técnico em Informática", duration=4, created_by=sentinel_user, updated_by=sentinel_user
        )
        food_course, food_created = Course.objects.get_or_create(
            name="Técnico em Alimentos", duration=4, created_by=sentinel_user, updated_by=sentinel_user
        )
        beekeeping_course, beekeeping_created = Course.objects.get_or_create(
            name="Técnico em Apicultura", duration=4, created_by=sentinel_user, updated_by=sentinel_user
        )

        self.log_course_creation_feedback(ads_course.name, ads_created)
        self.log_course_creation_feedback(agro_course.name, agro_created)
        self.log_course_creation_feedback(chem_course.name, chem_created)
        self.log_course_creation_feedback(it_course.name, it_created)
        self.log_course_creation_feedback(food_course.name, food_created)
        self.log_course_creation_feedback(beekeeping_course.name, beekeeping_created)
