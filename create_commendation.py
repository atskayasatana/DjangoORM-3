import argparse
import random

from datacenter.models import Commendation
from datacenter.models import Schoolkid
from datacenter.models import Lesson
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from sys import exit

commendations = ["Хвалю",
                 "Молодец",
                 "Хорошо проявил себя",
                 "Активно отвечал на все вопросы",
                 "Лучшая домашняя работа"
                ]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('name',
                        default=None)
    parser.add_argument('surname',
                        default=None)
    parser.add_argument('subject',
                        default=None)

    name = parser.parse_args().surname
    surname = parser.parse_args().name
    subject = parser.parse_args().subject

    if bool(name or surname or subject)is False:
        print('Для создания похвалы нужны имя, фамилия и предмет')
        exit()
    else:
        full_name = f'{surname} {name}'
        try:
            schoolkid = Schoolkid.objects.filter(
                                          full_name__contains=full_name).get()
        except MultipleObjectsReturned:
            print('Найдено более одного ученика с заданным именем')
            exit()
        except  ObjectDoesNotExist:
            print('Учеников с таким именем в базе нет')
            exit()
            
    try:
        lesson = random.choice(Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                                     group_letter=schoolkid.group_letter,
                                                     subject__title=subject).order_by('-date'))
    except  ObjectDoesNotExist:
            print('Ошибка в названии предмета')
            exit()
        
    Commendation.objects.create(text=random.choice(commendations),
                                created=lesson.date,
                                subject=lesson.subject,
                                teacher=lesson.teacher,
                                schoolkid=schoolkid)
    
    
