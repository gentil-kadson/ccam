from django.apps import AppConfig


class PeopleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ccam.people"

    def ready(self) -> None:
        from ccam.people import signals  # noqa: F401

        return super().ready()
