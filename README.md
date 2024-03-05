# Bulletin_Board
This is Django project - bulletin board for fans of fictional mmorpg
By default it uses postgresql DBMS.

Quick start:
1. Create virtual environment by "python -m venv venv"

2. Activate virtual environment by: "venv\Scripts\activate.bat" for Windows, "source venv/bin/activate" for Linux

3. Install required packages from PyPI by "pip install {package name}"

    Required packages from PyPI: django, psycopg2, django-summernote, python-dotenv, django-allauth, django-allauth[mfa],  django-filter

4. In the folder with "settings.py" create file ".env" with the following content:
    ```
    SECRET_KEY = 'your secret key'
    POSTGRES_PASS = 'password for postgres'
    POSTGRES_DB_NAME = 'database name'
    POSTGRES_USER = 'user`s name for postgres'
    POSTGRES_HOST  = 'postgres host name'
    POSTGRES_PORT = 'postgres port'
    YANDEX_HOST_USER = 'yanex host like yourappemail@yandex.ru'
    YANDEX_HOST_PASSWORD = 'password from your yandex email app'
    ```

5. Change data in ".env" file on your own

5. Make migrations by "python manage.py makemigrations"

6. Apply migrations by "python manage.py migrate"

7. Configure database by "python manage.py dbconfigure"

8. Run your project by ""python manage.py runserver"

PS: you can generate SECRET_KEY by function get_random_secret_key() from django.core.management.utils

PPS: if you don`t want to use postgresql, change variable DATABASES in "settngs.py" on:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }