from django.apps import AppConfig


class MainBoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Main_board'

    def ready(self):
        from . import signals