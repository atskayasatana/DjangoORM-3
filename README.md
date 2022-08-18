# DjangoORM
## Работа с электронным дневником

Для работы необходим Python3 и виртуальное окружение Django.
Скачиваем архив на свой компьютер и распаковываем в любую удобную директорию.
Запускаем среду выполнения и переходим в директорию проекта.
Перед запуском нужно подготовить .env файл окружения со следующей информацией:
```Python
DEBUG = True
SECRET_KEY = ... Ваш секретный ключ ...
ALLOWED_HOSTS = ... Разрешенные хосты ...
DATABASE_NAME = путь к базе данных, например: schoolbase.sqlite3
```
Файл нужно сохранить в директории проекта.

Установим зависимости из файла requirements.txt
```Python
pip install -r requirements.txt
```
Создадим виртуальное окружение(если оно не создано)
```Python
conda create -n djangoenv python=3.6 anaconda 
```
Перед началом работы окружение нужно активировать
```Python
  conda activate djangoenv
```
Запускаем сервер:
``` Python 
python manage.py runserver
```
Главная страница сайта:
![](https://github.com/atskayasatana/Images/blob/main/schoolkids.png "Главная страница")



