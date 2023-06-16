from django.apps import AppConfig


class TallerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taller'

class MecanicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mecanico'

class ClienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cliente'
