#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from protect_fields import *
class S_vol:
        #Данный класс описывает книгу, которая не имеет томов
        def __init__(self,author='',name='',year_p = 0,genre ='',location = 0,accessory = False,voluminous = False,archive = False ,comment_archive = '',data_creating,data_last_editing,data_archive):
                #author - автор книги
                #name - название книги
                #genre - жанар книги 
                # year_p - год издания книги;
                #accessory - чужая ли книга(True - чужая,False - своя);
                #location - полка, на которой находится книга
                #voluminous - признак многотомности книги
                self.author = author
                self.name = name
                self.year_p = year_p
                self.accessory = accessory
                self.genre = genre
                self.location = location
                self.voluminous = voluminous
		self.archive = archive
		self.comment_archive = comment_archive
		self.data_creating = data_creating
		self.data_last_editing = data_last_editing
		self.data_archive = data_archive
        def author_family(self):
        # Данная функция позволит получать Фамилию автора
                return self.author.split()[0]
        def author_initial(self):
        #Данная функция позволяет получить инициалы и фамию автора. 
                a1 = self.author.split()[1]
                a2 = self.author.split()[2]
                i1 = a1[0] + '.'+ a2[0]+'. '+ self.author.split()[0]
                return i1
        def save_db(self):
        #Данная функция сохраняет запись в БД
                file_db = shelve.open('book_db_1')
                K1 = []
                for key in file_db:
                        K1.append(key)
                cv = len(K1) 
                y = 'book'+str(cv)
                file_db[y] = self
                print ('Done record!')
                file_db.close()
        def author_name_middle_q(self):
        #Данная функция позволяет получить имя и отчество автора
                a1 = self.author.split()[1]
                a2 = self.author.split()[2]
                i1 = a1 +' '+ a2
                return i1
        def author_family_and_name_q(self):
        #Данная функция позволяет получить имя и фамилию автора
                a1 = self.author.split()[0]
                a2 = self.author.split()[1]
                i1 = a2 + ' ' + a1
                return i1
        #Подумать об оставшихся атрибутах - архивном атрибуте( и методе, который будет переводить книгу в архив) 
        #Реализовать метод редактирования уже существующих записей 
        #Зачатки графического интефейса - продумать каким образом он будет выглядеть - нарисовать окна, проудумать структуру.
