from django.apps import AppConfig


class CoordinatorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ccam.people.coordinators"

    def ready(self):
        from ccam.people.coordinators import signals  # noqa: F401

        return super().ready()
