#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from new_record import *
from search import *
print('Выберете действие:\n1.Внесесение записи в базу данных\n2.Поиск книг в базе данных(не работает)\n3.Изменение в записи базы данных(не работает)\n4.Удаление записи из базы данных(не работает)')
in00 = input('Введите нужны пункт меню:')
if in00 == '1':
        j = new_record()
        K=[]
        db_f = shelve.open('book_db_2')
        print('Последние 15 записей:')
        for key in db_f:
                K.append(key)
                li = 0
                if li <15:
                        print('\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
                else: pass
        print('Всего записей в базе данных:',len(K))

elif in00 =='2':
        search_full_name()
elif in00 =='3':
        print('ВРЕМЕННО НЕ РАБОТАЕТ')
elif in00 =='4':
        print('ВРЕМЕННО НЕ РАБОТАЕТ')
