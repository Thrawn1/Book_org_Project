#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from protect_fields import *
class S_vol:
        #Данный класс описывает книгу, которая не имеет томов
        def __init__(self,author='',name='',year_p = 0,genre ='',location = 0,accessory = False):
                #author - автор книги
                #name - название книги
                #genre - жанар книги 
                # year_p - год издания книги;
                #accessory - чужая ли книга(True - чужая,False - своя);
                #location - полка, на которой находится книга
                self.author = author
                self.name = name
                self.year_p = year_p
                self.accessory = accessory
                self.genre = genre
                self.location = location
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
        #Подумать об оставшихся атрибутах - архивном атрибуте( и методе, который будет переводить книгу в архив) 
        #Реализовать поиск в виде метода, которому передается ключ поиска. Правда вопрос, надо ли так делать? 
        #Реализовать метод редактирования уже существующих записей 
        #Зачатки графического интефейса - продумать каким образом он будет выглядеть - нарисовать окна, проудумать структуру.
#	def search_book_name(self):
#		R = []
#		in1 = input()
#		if in1 == S_vol.name:
#			R.append(S_vol.name+' '+ S_vol.author)
#			return R
#		else: 
#			pass
#    def search_book_author(self):
#        
#        
#    def dump_db(self):
#
#    def update(self):
