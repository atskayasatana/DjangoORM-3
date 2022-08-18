import argparse

from datacenter.models import Schoolkid
from datacenter.models import Chastisement

from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from sys import exit

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('schoolkid_name',
                        nargs='+',
                        default=None)
    
    schoolkid_name = ' '.join(parser.parse_args().schoolkid_name)
    
    if not schoolkid_name or schoolkid_name in (' ',''):
        print('Введите имя ученика')
        exit()
    else:
        try:
            schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid_name).get()
        except MultipleObjectsReturned:
            print('Найдено более одного ученика с заданным именем!')
            print('Уточните параметры поиска')
            exit()
        except  ObjectDoesNotExist:
            print('Учеников с таким именем в базе нет')
            print('Уточните параметры поиска')
            exit()

    kid_chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    kid_chastisement.delete()
