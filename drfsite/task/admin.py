from django.contrib import admin
from .models import Task

# Регистрируем модель Task в административной панели Django
# Это позволит нам управлять объектами модели Task через интерфейс администратора
admin.site.register(Task)
