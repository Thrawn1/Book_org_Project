#! /usr/bin/env python
# -*- coding: utf-8 -*-
from menu_all_search import *
from add_book_func import *
from update_book_func import *
def menu ():
        print('Выберете действие:\n\n\n1.Внеcение записи в базу данных\n\n2.Поиск книг в базе данных\n\n3.Изменение в записи базы данных\n\n4.Удаление записи из базы данных(не работает)')
        in00 = input('\nВведите нужны пункт меню:')
        if in00 == '1':
                add_book_func()
        elif in00 =='2':
                in_2 = input('\n\nВведите количество резульатов поиска,отображаемых на экране: ')
                menu_all_search(in_2)
        elif in00 =='3':
                update_book_func()
        elif in00 =='4':
                print('ВРЕМЕННО НЕ РАБОТАЕТ')
        else: 
                print ('Введен не верный пункт меню или не допустимое значение!')
