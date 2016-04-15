#! /usr/bin/env python
# -*- coding: utf-8 -*-
from s_vol_c import *
from m_vol_c import *
import shelve
def search_family(in1):
#Поиск по фамили автора
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
#Поиск по названию книги
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
# Поиск по имени-отчеству автора
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
def search_initials_family(in1):
# Поиск по фамилии и инициалам
        R = []
        K = []
        nm = 0
        db_f = shelve.open('book_db_2')
        for key in db_f:
                K.append(key)
        j = input('\nВведите инициалы и с пробелом фамилию автора: ')
        for b in K:
                c = db_f[b].author_initial()
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
def search_full_author(in1):
# Поиск по Фамилии-Имени-Отчеству
        R = []
        K = []
        nm = 0
        db_f = shelve.open('book_db_2')
        for key in db_f:
                K.append(key)
        j = input('\nВведите фамилию, имя, отчество через пробел: ')
        for b in db_f:
                c = db_f[b].author
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

def search_name_and_family(in1):
#Поиск по фамилии и имени
        R = []
        K = []
        nm = 0
        db_f = shelve.open('book_db_2')
        for key in db_f:
                K.append(key)
        j = input('\nВведите имя и фамилию автора через один пробел: ')
        for b in K:
                c = db_f[b].author_family_and_name_q()
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
