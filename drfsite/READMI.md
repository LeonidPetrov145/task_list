# Инструкция по работе с системой     
 




# Скачать небоходимые файлы с гидхаб 
 
https://github.com/LeonidPetrov145/task

# Установить нужные для работы библиотеки  
pip install django  

pip install djangorestframework 

pip install django-filters 

pip install djangorestframework-simplejwt 

pip install pip install psycopg2 
 

# Запустьть систему через консоль введя команду  
Команда - python manage.py runserver 
 

# Вводить маршруты после https://127.0.0.1:8000/

# После перехода по этой ссылке будут доступны эти маршруты
    http://127.0.0.1:8000/tasks/       #Маршрут сортировки по статусу 
    http://127.0.0.1:8000/categories/  #Маршрут сортировки по категириям
    http://127.0.0.1:8000/items/       #Маршрут сортировки по названию, можно по алфавиту или наоборот
    Команды для маршрутов связаных с сортировкой
# Маршруты
    # Маршрут для административной панели Django 
    admin/ 
     
    # Маршрут для аутентификации через DRF  
    api/v1/drf-auth/ 
     
    # Маршрут для отображения списка задач и создания новых задач 
    api/v1/tasklist/ 
     
    # Маршрут для обновления и получения конкретной задачи по её ID 
    api/v1/task/<int:pk>/ 
     
    # Маршрут для удаления конкретной задачи по её ID 
    api/v1/taskdelate/<int:pk>/ 
     
    # Маршрут для аутентификации через Djoser  
    api/v1/auth/ 
     
    # Маршрут для получения пары токенов access и refresh 
    api/token/ 
     
    # Маршрут для обновления токена доступа (access token) 
    api/token/refresh/ 
     
    # Маршрут для проверки валидности токена 
    api/token/verify/ 
 
 
# Если чтото не работает обращайтесь суда:@LeonidPochtiIlich - Telegram, +7(996)-644-31-60