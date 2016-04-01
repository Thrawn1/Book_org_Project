#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from s_vol_c import *
from m_vol_c import *
from new_record import *
j = new_record()
K=[]
db_f = shelve.open('book_db_2')
for key in db_f:
        K.append(key)
        print('\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')    
print(K)

#db = [book0,book1,book2,book3,book4,book5]
#R = []
#j = input('Введите имя автора:')
#for b in db:
#	c = b.author_family()
#	if j == c:
#		R.append(b.author_initial()+' ; '+ b.name)
#	else: pass
#print(R) 
