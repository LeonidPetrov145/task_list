from django.apps import AppConfig


# Создаем класс конфигурации для приложения "task"
class TaskConfig(AppConfig):
    # Устанавливаем поле по умолчанию для автоматически генерируемых первичных ключей
    # В данном случае используется BigAutoField, который является 64-битным целым числом
    default_auto_field = 'django.db.models.BigAutoField'

    # Указываем имя приложения, которое будет использоваться в конфигурации Django
    name = 'task'