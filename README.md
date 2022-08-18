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

Главная страница сайта http://127.0.0.1:8000/:
![](https://github.com/atskayasatana/Images/blob/main/schoolkids.png "Главная страница")

## Основные скрипты

Скрипты можно запускать в интерактивной shell оболочке

```Python
python manage.py shell
```
Перед запуском нужно импортировать функции:

```
import fix_marks, create_commendation, remove_chastisement

```

### fix_marks.py
Исправляет оценки 2 и 3 на 5. Обязательным аргументом является имя ученика, для которого нужно исправить оценки.
```
run fix_marks.py Фамилия Имя
```
Если в школе есть еще один ученик с указанными именем и фамилией, то функция вернет сообщение об этом('Найдено более одного ученика с заданным именем!') и не сработает. 
Также функция вернет сообщение об ошибке, если ученик не найден: 'Учеников с таким именем в базе нет'

### remove_chastisement.py
Удаляет все замечания ученика с заданными именем и фамилией.

```
run remove_chastisement.py Фамилия Имя
```
Если в школе есть еще один ученик с указанными именем и фамилией, то функция вернет сообщение об этом('Найдено более одного ученика с заданным именем!') и не сработает. 
Также функция вернет сообщение об ошибке, если ученик не найден: 'Учеников с таким именем в базе нет'

### create_commendations.py

Создает похвалы ученику от учителя заданного предмета.

```
run create_commendations.py Фамилия Имя Предмет

```
Дата для похвалы выбирается случайно из дат всех уроков по заданному предмету, текст похвалы берется случайным образом из списка commendations в файле скрипта.
Если один из аргументов не был указан, то функция вернет сообщение об ошибке: 'Для создания похвалы нужны имя, фамилия и предмет'
Если в школе есть еще один ученик с указанными именем и фамилией, то функция вернет сообщение об этом('Найдено более одного ученика с заданным именем!') и не сработает. 
Также функция вернет сообщение об ошибке, если ученик не найден: 'Учеников с таким именем в базе нет'
Если в школе нет предмета, который передан в качетсве аргумента, то появится сообщение:'Ошибка в названии предмета'

После того, как все нужные скрипты отработали можно выйти из shell:ctrl+D и клавиша y после вопроса Do you really want to exit ([y]/n)?

На сайте на странице ученика можно будет увидеть результат работы, например, новые похвалы:
![](https://github.com/atskayasatana/Images/blob/e6117dcdd677f622c091439c521c9bed6f693c3c/commentation.png "Похвалы")











