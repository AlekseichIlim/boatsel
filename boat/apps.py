from django.apps import AppConfig


class BoatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boat'
    verbose_name = 'лодки'
#     verbose_name - название приложения в админке