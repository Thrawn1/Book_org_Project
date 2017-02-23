from s_vol_c import *
from m_vol_c import *
from sort_foreign_author import *
from definition_author import *
from protect_fields import *
import shelve
def search_family(in1,db_f):
#Поиск по фамили автора
    R = []
    K = []
    nm = 0
    for key in db_f:
                K.append(key)
    j1 = input('\nВведите фамилию автора: ')
    j = j1.lower()
    for b in K:
        c1 = db_f[b].author_family
        c = c1.lower()
        if j == c and nm < in1:
                R.append(b)
                nm = nm+1
        else:
                pass
    if len(R) !=0:
        return R
    else:
        print('\nНичего не найдено!')

def search_name_book(in1,db_f):
#Поиск по названию книги
    R = []
    K = []
    nm = 0
    for key in db_f:
                K.append(key)
    j1 = input('\nВведите имя название книги: ')
    j2 = j1.replace(' ','')
    j3 = j2.replace('.','')
    j4 = j3.lower()
    for b in K:
            n = db_f[b].name_book
            n1 = n.replace(' ','')
            n2 = n1.replace('.','')
            n3 = n2.lower()
            if j4 == n3 and nm < in1:
                R.append(b)
                nm = nm + 1
            else:
                pass
    if len(R) !=0:
        return R
    else:
        print('\n\n\n\n\nНичего не найдено!')
        return R
def search_middle_name(in1,db_f):
# Поиск по имени-отчеству автора
        R = []
        K1 = []
        nm = 0
        for key in db_f:
                K1.append(key)
        jd = definition_author()
        if jd == 1:
                j1 = input('\nВведите имя и отчество  автора: ')
                K = sort_foreign_author(1,K1,db_f)
                j2 = j1.replace(' ','')
                j = j2.lower()
        elif jd == 2:
                j1 = input('\nВведите имя и второе имя зарубежного автора: ')
                K = sort_foreign_author(2,K1,db_f)
                j2 = j1.replace(' ','')
                j = j2.lower()
        else:
                print('Ошибка!')
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
        j1 = input('\nВведите инициалы и фамилию автора: ')
        j2 = j1.replace(' ','')
        j3 = j2.replace('.','')
        j = j3.lower() 
        for b in K:
                c = db_f[b].author_initial()
                for m in c:
                        if m == j and nm < in1:
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
        K1 = []
        nm = 0
        for key in db_f:
                K1.append(key)
        jd = definition_author()
        if jd == 1:
                j1 = input('\nВведите фамилию, имя и отчество  автора: ')
                K = sort_foreign_author(1,K1,db_f)
                j2 = j1.replace(' ','')
                j = j2.lower()
        elif jd == 2:
                j1 = input('\nВведите имя,второе имя и фамилию зарубежного автора: ')
                K = sort_foreign_author(2,K1,db_f)
                j2 = j1.replace(' ','')
                j = j2.lower()
        for b in db_f:
                c1 = str(db_f[b].author_family) + str(db_f[b].author_name) + str(db_f[b].author_middle_name)
                c2 = str(db_f[b].author_middle_name) + str(db_f[b].author_name) + str(db_f[b].author_family)
                c3 = str(db_f[b].author_name) + str(db_f[b].author_middle_name) + str(db_f[b].author_family)
                c11 = c1.lower()
                c22 = c2.lower()
                c33 = c3.lower()
                if j == c11 or j == c22 or j == c33 and nm < in1:
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
        j1 = input('\nВведите имя и фамилию автора: ')
        j2 = j1.replace(' ','')
        j3 = j2.replace('.','')
        j = j3.lower()
        for b in K:
                c = db_f[b].author_name_and_family()
                c1 = c[0]
                c2 = c[1]
                if j == c1 or j == c2 and nm < in1:
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
        R = []
        K = []
        nm = 0
        for key in db_f:
                K.append(key)
        j1 = input('\nВведите жанр книги: ')
        j2 = j1.replace(' ','')
        j3 = j2.replace('.','')
        j4 = j3.lower()
        for b in K:
                s = db_f[b].genre
                s1 = s.replace(' ','')
                s2 = s1.replace('.','')
                s3 = s2.lower()
                if j3 == s3 and nm < in1:
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
        R = []
        K = []
        nm = 0
        trt = 0
        for key in db_f:
                K.append(key)
        while trt != 1:
                j = input('\nВведите год издания: ')
                trt = protect_date(j)
                if trt == 1:
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
        R = []
        K = []
        nm = 0
        trt = 0
        for key in db_f:
                K.append(key)
        while trt != 1:
                j = input('\nВведите номер полки, список книг с которой вы хотите получить: ')
                trt= protect_location(j)
                if trt ==1 : 
                        for b in K:
                                c = db_f[b].location
                        if j == str(c) and nm < in1:
                                R.append(b)
                                nm = nm+1
                        else:
                                pass
                else:
                        pass
        if len(R) !=0:
                return R
        else:
                print('\nНичего не найдено!')
                return []
def search_archive():
        pass
