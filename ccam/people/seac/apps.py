from django.apps import AppConfig


class SeacConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ccam.people.seac"

    def ready(self):
        from ccam.people.seac import signals  # noqa: F401

        return super().ready()
