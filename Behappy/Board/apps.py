from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'

    
class BoardConfig(AppConfig):
    name = 'Board'
