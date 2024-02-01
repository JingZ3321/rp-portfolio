# contains settings for the application configuration

from django.apps import AppConfig


class MyprotfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyProtfolio'
