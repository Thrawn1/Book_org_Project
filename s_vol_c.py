#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
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
                return self.author.split()[2]
        def author_initial(self):
        #Данная функция позволяет получить инициалы и фамию автора. 
                a1 = self.author.split()[0]
                a2 = self.author.split()[1]
                i1 = a1[0] + '.'+ a2[0]+'. '+ self.author.split()[2]
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
        def new_record(self):#Данная функция создает новую запись в БД
        	file_db = shelve.open('book_db_2')
        	K1 = []
        	for key in file_db:
        		K1.append(key)
        	cv = len(K1) 
        	y = 'book'+str(cv)
        	print('Выберете, какой тип книги хотите добавить:\n1.Однотомная книга \n2.Многотомное собрание сочинений(пока не работает)')
        	type_in = input('Введите пункт меню:')
        	if type_in == '1':
        		fieldnmes = ('author','name','year_p','genre','location','accessory')
        		fieldnmes_1 = ('Автор книги','Название книги','Год издания','Жанр','Где расположена книга','Чужая ли книга?')
        		rt = 0
        		for field in fieldnmes:
        			field_1 = fieldnmes_1[rt]
        			if field == 'year_p':
        				new_b = input('\t[%s]\nВведите год издания=>' % (field_1))
        				setattr(self,field,eval(new_b))
        				rt = rt+1
        			elif field == 'location':
        				new_b = input('\t[%s]\nВведите номер полки=>' % (field_1))
        				setattr(self,field,eval(new_b))
        				rt = rt+1

        			elif field == 'accessory':
        				print('Пожалуйста выберете один из вариантов:\n1. Книга ваша\n2. Книга чужая')
        				new_b = int(input('\t[%s]\n:' % (field_1)))
        				if new_b == 1:
        					setattr(self,field,False)
        					rt = rt+1
        				elif new_b == 2:
        					setattr(self,field,True)
        					rt = rt+1
        				else:
        					print('Выбрано недопустимое значение!')
        			else:
        				new_b_1 = input('\t[%s]\nВведите значение =>' % (field_1))
        				new_b = '\''+str(new_b_1)+'\''
        				setattr(self,field,eval(new_b))
        				rt = rt+1
        	elif type_in =='2':
        		fieldnmes = ('author','name','year_p','genre','location','accessory','total_vol','number_vol','availble_vol')
        		pass
        	else:
        		print('\nВведено не верное значение!')
        	file_db[y]=self
        	file_db.close()
        	print('\nЗапись занесена!')
        	return 1
        #Необходимо реализовать проверку заполенения полей. Поле Год должно проверяться на ввод текста и диапазона значений. Поле полка так же должно проверятся. 
        #Подумать об оставшихся атрибутах - архивном атрибуте( и методе, который будет переводить книгу в архив) 
        #Реализовать поиск в виде метода, которому передается ключ поиска. Правда вопрос, надол ли так делать? 
        #Реализовать защиту от введения пустых значений в полях Автор, Навзавние книги, Номер полки. Пункт принадлежности книги уже защищен
        #Реализовать метод редактирования уже существующих записей 
        #Зачатки графического интефейса - продумать каким образом он будет выглядеть - нарисовать окна, проудумать структуру.
        #Дописать функцию добавления для многотомников. Использовать расширение методов.  
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
