 #! /usr/bin/env python
# -*- coding: utf-8 -*-
from menu import *
n = 0
while n != 1:
    db_f = shelve.open('book_db_2')
    menu(db_f)
    db_f.close()
    
# Стартовй файл(с него начинается выполнение программы). В данном случае он взывает всего одну функцию - menu, котрая занимается построением меню) 
