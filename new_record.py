#! /usr/bin/env python
# -*- coding: utf-8 -*-
from m_vol_c import *
from s_vol_c import *
from new_record_s import *
from new_record_m import *
import shelve
def new_record():
    #Данная функция создает новую запись в БД
    file_db = shelve.open('book_db_2')
    K1 = []
    for key in file_db:
        K1.append(key)
    cv = len(K1) 
    y = 'book'+str(cv)
    print('Выберете, какой тип книги хотите добавить:\n1.Однотомная книга \n2.Многотомное собрание сочинений')
    type_in = input('Введите пункт меню:')
    if type_in == '1':
        j = S_vol()
        t = single_book(j)
    elif type_in =='2':
        j = M_vol()
        t1 = single_book(j)
        t = multi_book(t1)
    else:
        print('\nВведено не верное значение!')
    file_db[y]=t
    file_db.close()
    print('\nЗапись занесена!')
    return 1
