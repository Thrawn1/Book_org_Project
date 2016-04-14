#! /usr/bin/env python
# -*- coding: utf-8 -*-
from s_vol_c import *
from m_vol_c import *
import shelve
def search_family(in1):
    R = []
    K = []
    nm = 0
    db_f = shelve.open('book_db_2')
    for key in db_f:
                K.append(key)
    j = input('\nВведите фамилию автора: ')
    for b in K:
            c = db_f[b].author_family()
            if j == c and nm < in1:
                R.append(b)
                nm = nm+1
            else:
                pass
    if len(R) !=0:
        return R
    else:
        print('\nНичего не найдено!')

def search_name(in1):
    R = []
    K = []
    nm = 0
    db_f = shelve.open('book_db_2')
    for key in db_f:
                K.append(key)
    j = input('\nВведите имя название книги: ')
    for b in K:
            c = db_f[b].name
            if j == c and nm < in1:
                R.append(b)
                nm = nm + 1
            else:
                pass
    if len(R) !=0:
        return R
    else:
        print('\nНичего не найдено!')
def search_middle_name(in1):
    R = []
    K = []
    nm = 0
    db_f = shelve.open('book_db_2')
    for key in db_f:
                K.append(key)
    j = input('\nВведите имя и отчество автора: ')
    for b in K:
            c = db_f[b].author_name_middle_q()
            if j == c and nm < in1:
                R.append(b)
                nm = nm+1
            else:
                pass
    if len(R) !=0:
        return R
    else:
        print('\nНичего не найдено!')
        return []
