from django.apps import AppConfig

class MyAppConfig(AppConfig):

    name = 'web'

    def ready(self):
        import web.signals
