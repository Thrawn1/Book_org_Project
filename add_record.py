#! /usr/bin/env python
# -*- coding: utf-8 -*-
from s_vol_c import *
from m_vol_c import *
import shelve
def new_record(self):#Данная функция создает новую запись в БД
	file_db = shelve.open('book_db_1')
	K1 = []
	for key in file_db:
		K1.append(key)
	cv = len(K1) 
	y = 'book'+str(cv)
	print('Выберете какой тип книги хотите добавит:\n1.Однотомная книга \n2.Двухтомная книга')
	type_in = input('Введите значение:')
	if type_in == '1':
		fieldnmes = ('author','name','year_p','genre','location','accessory')
		fieldnmes_1 = ('Автор','Наименование','Год издания','Жанр','Местоположение','Чужая ли книга?')
		rt = 0
		for field in fieldnmes:
				field_1 = fieldnmes_1[rt]
				new_b = input('\t[%s]\nnew?=>' % (field_1))
				setattr(self,field,eval(new_b))
				print('Done new!')
				rt = rt+1
	elif type_in =='2':
		fieldnmes = ('author','name','year_p','genre','location','accessory','total_vol','number_vol','availble_vol')
		pass
	else:
		print('\nВведено не верное значение!')
	file_db[y]=self
	file_db.close()
	return 1
