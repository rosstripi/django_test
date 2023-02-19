from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "vue_django_template.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import vue_django_template.users.signals  # noqa F401
        except ImportError:
            pass
