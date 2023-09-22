## Курсовая 7. DRF

### 1. Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:

    Команда для Windows:
        - python -m venv venv
        - venv\Scripts\activate
        - pip install -r requirements.txt

    Команда для Unix:
        - python3 -m venv venv
        - source venv/bin/activate 
        - pip install -r requirements.txt

### 2. Создайте базу данных:

        - psql -U postgres
        - CREATE DATABASE ob_db;
        - \q

### 3. Для заполнения моделей данными необходимо выполнить следующую команду:

    Команда для Windows:
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py loaddata data.json

    Команда для Unix:
        - python manage.py makemigrations
        - python manage.py migrate
        - python3 manage.py loaddata data.json

### 4. Для работы с переменными окружениями необходимо создать и заполнить файл .env:

    # Database
    POSTGRES_DB='ob_db'
    POSTGRES_USER='postgres'
    POSTGRES_PASSWORD=/ваш пароль/
    POSTGRES_HOST='127.0.0.1'
    POSTGRES_PORT=/обычно это'5432'/

    - SECRET_KEY=/ключ Django из файла config.settings/

### 5. Для создания администратора (createsuperuser):

    - заполните поля email, PASSWORD. users/management/commands/csu.py
    Команда для Windows
    - python manage.py csu

    Команда для Unix
    - python3 manage.py csu

### 6. Для запуска приложения:

    Команда для Windows:
    - python manage.py runserver

    Команда для Unix:
    - python3 manage.py runserver

### 7. Для запуска тестов:

    - coverage run --source='.' manage.py test
    - coverage report