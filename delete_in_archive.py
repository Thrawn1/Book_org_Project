#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
import datetime
from key_book_sort import *
def delete_in_archive(db_f):
        K = []
        R = []
        tmp = 1
        tmp1 = 0
        for key in db_f:
                K.append(key)
                R.append(tmp)
                tmp = tmp + 1
        K1 = key_book_sort(K)
        for b in K1:
                num1 = R[tmp1]
                n = db_f[b].voluminous
                h = db_f[z1].accessory_type()
                if n == False:
                        print('\n','\t',num1,'.','   [',db_f[b].author_name,db_f[b].author_middle_name,db_f[b].author_family,db_f[b].name_book,db_f[b].year_p,db_f[b].genre,h,('Полка №'+str(db_f[b].location)),']','\n ')
                elif n == True:
                        print('\n','\t',num1,'.','   [',db_f[b].author_name,db_f[b].author_middle_name,db_f[b].author_family,db_f[b].name_book,db_f[b].year_p,db_f[b].genre,h,('Всего томов: '+str(db_f[b].total_vol)),('Номер тома: '+str(db_f[b].number_vol)),('Всего томов в библиотеке: '+str(db_f[b].availble_vol)),('Полка №'+str(db_f[b].location)),']','\n')
                else:
                        print('Ошибка определения многотмности')
                tmp1 = tmp1 + 1 
        in11 = input('Введите ключ записи, которую хотите отправить в архив: ')
        ttt = 0
        while ttt !=1:
                y = int(in11) in R
                z = int(in11) - 1
                if y == True and z >= 0:
                        z1 = K[z]
                        arc_book = db_f[z1]
                        setattr(arc_book,'archive',True)
                        ttt1 = 0
                        while ttt1 != 1:
                                comm=input('Введите комментарий к удалению в архив. Внимание, комментарий не может быть пустым!\n\n')
                                n = len(comm)
                                m = comm.isalpha()
                                print(n,m,comm)
                                if n > 0 and m == True:
                                        ttt1 = 1
                                        setattr(arc_book,'comment_archive',comm)
                                else:
                                        print('Не введен комментарий или введен не корректно')
                        time = datetime.datetime.now()
                        date_str = time.strftime("%d-%m-%Y")
                        setattr(arc_book,'data_archive',date_str)
                        db_f[z1] = arc_book
                        print('\n\n\tЗапись успешно занесена в архив!')
                        h1 = db_f[z1].accessory_type()
                        jj = db_f[z1].archive_type()
                        gg = db_f[z1].voluminous_type()
                        print('\n\n','\t',gg,'   ',db_f[z1].author_name,db_f[z1].author_middle_name,db_f[z1].author_family,db_f[z1].name_book,db_f[z1].year_p,db_f[z1].genre,h1,jj,db_f[z1].data_archive,db_f[z1].comment_archive)
                        db_f.close()
                        ttt = 1
                else:
                        print('Введите корректный номер записи!')
