# Тестовое задание для кандидатов-разработчиков в ООО Фабрика Решений, на должность Python-разработчик (Django, DRF). 
# Тестовое задание: https://www.craft.do/s/n6OVYFVUpq0o6L

##### _разработка Sayfullin R.R. 

Инструкция актуальна для Linux-систем.
========================================================================================================================

Скопируйте репозиторий с помощью команды:
$ git clone https://github.com/RuslanSayfullin/notification_services.git
Перейдите в основную директорию с помощью команды: 
$ cd notification_service

Создать и активировать виртуальное окружение:
========================================================================================================================
$ poetry env use python3.11
Установить зависимости:
$ poetry install 
Сохранить, адрес созданного виртуального окружения из вывода(рекомендуется)
$ poetry shell
(web-py3.11) $
Выход:
$ exit

/home/user/.cache/pypoetry/virtualenvs/

Добавить в директорию notification_services/service файл psw.py
========================================================================================================================
В данный файл, необходимо добавить две переменные:

secret_key = 'ваш секретный ключ'   # секретный ключ приложения
dbase_psw = 'ваш ключ к БД'         # Пароль для подключения к БД

Создание БД
========================================================================================================================
Войдите в интерактивный сеанс Postgres, набрав:
$ sudo -u postgres psql


=# CREATE DATABASE service;
=# CREATE USER service WITH PASSWORD 'myPassword';
=# GRANT ALL PRIVILEGES ON DATABASE service TO portaluser;
=# \q
$ exit

Перейти в директорию notification_services
========================================================================================================================
Для запуска выполнить следующие команды:
Команда для создания миграций приложения для базы данных
$ python3 manage.py makemigrations
$ python3 manage.py migrate

Создание суперпользователя
$ python3 manage.py createsuperuser

Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:
по умолчанию почта admin@admin.com пароль: 12345

Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.

Команды для запуска приложения:
$ python3 manage.py runserver


Django-приложение будет доступно по адресу: http://127.0.0.1:8000/



