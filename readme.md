### Установка
---

#### Шаг 1:

Запустить виртуальное окружение

#### Шаг 2:

Установить необходимые зависимости

```shell
    pip install -r requirements.txt
```


#### Шаг 3:

Изменить файл max/settings.py

#### Шаг 4:

Применить миграцию на базу 

```shell
    python manage.py migrate
```

#### Шаг 4.5 (при первом запуске):

Создать суперюзера

```shell
    python manage.py createsuperuser
```

#### Шаг 5:

Запуск сервера

```shell
    python manage.py runserver
```

