from s_vol_c import *
from m_vol_c import *
import shelve
def search_family(in1,db_f):
#Поиск по фамили автора
    R = []
    K = []
    nm = 0
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

def search_name(in1,db_f):
#Поиск по названию книги
    R = []
    K = []
    nm = 0
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
def search_middle_name(in1,db_f):
# Поиск по имени-отчеству автора
    R = []
    K = []
    nm = 0
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
def search_initials_family(in1,db_f):
# Поиск по фамилии и инициалам
        R = []
        K = []
        nm = 0
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
def search_full_author(in1,db_f):
# Поиск по Фамилии-Имени-Отчеству
        R = []
        K = []
        nm = 0
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

def search_name_and_family(in1,db_f):
#Поиск по фамилии и имени
        R = []
        K = []
        nm = 0
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
def search_genre_book(in1,db_f):
        pass
        R = []
        K = []
        nm = 0
        for key in db_f:
                K.append(key)
        j = input('\nВведите жанр книги: ')
        for b in K:
                c = db_f[b].genre
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
def search_year_pub(in1,db_f):
        pass
        R = []
        K = []
        nm = 0
        for key in db_f:
                K.append(key)
        j = input('\nВведите год издания: ')
        for b in K:
                c = db_f[b].year_p
                if j == str(c) and nm < in1:
                        R.append(b)
                        nm = nm+1
                else:
                        pass
        if len(R) !=0:
                return R
        else:
                print('\nНичего не найдено!')
                return []
def search_location(in1,db_f):
        pass
        R = []
        K = []
        nm = 0
        for key in db_f:
                K.append(key)
        j = input('\nВведите номер полки, список книг с которой вы хотите получить: ')
        for b in K:
                c = db_f[b].location
                if j == str(c) and nm < in1:
                        R.append(b)
                        nm = nm+1
                else:
                        pass
        if len(R) !=0:
                return R
        else:
                print('\nНичего не найдено!')
                return []
def search_archive():
        pass
