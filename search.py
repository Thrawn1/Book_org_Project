#! /usr/bin/env python
# -*- coding: utf-8 -*-
from s_vol_c import *
from m_vol_c import *
import shelve
def search_family():
    R = []
    K = []
    db_f = shelve.open('book_db_2')
    for key in db_f:
                K.append(key)
    j = input('Введите имя автора:')
    for b in K:
            c = db_f[b].author_family()
            if j == c:
                R.append(db_f[b].author_initial()+' ; '+ db_f[b].name)
            else:
                pass
    if len(R) !=0:
        print(R)
    else:
        print('Ничего не найдено!')
    
