#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from search import *
from protect_fields import *
from menu_search_author import *
def menu_all_search(in_2):
        in_tmp_2 = protect_number(in_2)
        if in_tmp_2 == 1:
                print('\n\nПожалуйста, выберете тип поиска:\n\n1.Поиск по названию книги\n\n2.Поиск по автору\n\n3.Поиск по жанру\n\n4.Поиск по году издания\n\n5.Поиск по полке\n\n6. *Произвольный поиск(будет реализован много позднее)\n\n')
                in_1 = input('\n\nВведите номер пункта меню: ')
                if in_1 == '1':
                # Поиск по названию книги
                        z = search_name(int(in_2))
                        db_f = shelve.open('book_db_2')
                        for key in z:
                                print('\n','\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
                elif in_1 == '2':
                # Вызов меню для различных вариантов поиска по автору
                        n = menu_search_author (in_2)
                elif in_1 == '3':
                        z = search_genre_book(int(in_2))
                        db_f = shelve.open('book_db_2')
                        for key in z:
                                print('\n','\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
                elif in_1 == '4':
                        pass
                        z = search_year_pub(int(in_2))
                        db_f = shelve.open('book_db_2')
                        for key in z:
                                print('\n','\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
                elif in_1 == '5':
                        pass
                        z = search_location(int(in_2))
                        db_f = shelve.open('book_db_2')
                        for key in z:
                                print('\n','\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
                elif in_1 == '6':
                        print('ВРЕМЕННО НЕ РАБОТАЕТ')
                else: pass
        else:
                pass
