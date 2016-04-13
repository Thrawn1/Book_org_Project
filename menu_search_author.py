#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from new_record import *
from search import *
from protect_fields import *
def menu_search_author (in2):
        print('\n\nВыберете вариант поиска по фамилии:\n\n1.Поиск только по фамилии2.Поиск по фамилии и имени\n\n3.Поиск по Фамилии и инициалам\n\n4.Поиск по имени-отчеству\n\n5. *Произвольный поиск(будет реализован много позднее\n\n')
# - в нем поиск будет производится в рамках введеных символов, без обязательной привязки к полям')
        in_3 = input('Введите номер пункта меню:')
        if in_3 == '1':
                z = search_family(int(in_2))
                db_f = shelve.open('book_db_2')
                for key in z:
                        print('\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
        elif in_3 == '2':
                z = search_full_author(int(in_2))
                db_f = shelve.open('book_db_2')
                for key in z:
                        print('\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
        elif in_3 == '3':
                z = search_initials_family(int(in_2))
                db_f = shelve.open('book_db_2')
                for key in z:
                        print('\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
        elif in_3 == '4':
                z = search_middle_name(int(in_2))
                db_f = shelve.open('book_db_2')
                for key in z:
                        print('\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n') 
        else: print('Ошибка')
