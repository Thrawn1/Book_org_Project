#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from search import *
from protect_fields import *
from menu_search_author import *
def menu_all_search():
        print('\n\nПожалуйста, выберете тип поиска:\n\n1.Поиск по названию книги\n\n2.Поиск по автору\n\n3.Поиск по жанру\n\n4.Поиск по году\n\n5.Поиск по полке\n\n')
        in_1 = input('\n\nВведите номер пункта меню:')
        in_2 = input('\n\nzВведите количество резульатов поиска,отображаемых на экране:')
        in_tmp_2 = protect_number(in_2)
        if in_tmp_2 == 1:
                if in_1 == '1':
                        z = search_name(int(in_2))
                        db_f = shelve.open('book_db_2')
                        for key in z:
                                print('\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
        elif in_1 == '2':
                menu_search_author (in2)
        else: pass
