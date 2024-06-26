from django.apps import AppConfig


class GymAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GYM_APP'

    def ready(self):
        import GYM_APP.Models
        import GYM_APP.Serializers
        import GYM_APP.Views
        import GYM_APP.Urls