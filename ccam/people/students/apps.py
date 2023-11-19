from django.apps import AppConfig


class StudentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ccam.people.students"

    def ready(self):
        from ccam.people.students import signals  # noqa: F401

        return super().ready()
