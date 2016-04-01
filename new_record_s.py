#! /usr/bin/env python
# -*- coding: utf-8 -*-
from protect_fields import *
def single_book(self):
    fieldnmes = ('author','name','year_p','genre','location','accessory')
    fieldnmes_1 = ('Автор книги','Название книги','Год издания','Жанр','Где расположена книга','Чужая ли книга?')
    rt = 0
    for field in fieldnmes:
        cb = 0
        field_1 = fieldnmes_1[rt]
        if field == 'year_p':
            while cb != 1:
                new_b = input('\t[%s]\nВведите год издания:' % (field_1))
                cb = protect_date(new_b)
                if cb == 1:
                    setattr(self,field,eval(new_b))
                    rt = rt+1
                else: pass
        elif field == 'location':
            while cb != 1:
                new_b = input('\t[%s]\nВведите номер полки:' % (field_1))
                cb = protect_location(new_b)
                if cb == 1:
                    setattr(self,field,eval(new_b))
                    rt = rt+1
                else: pass
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
        elif field == 'genre':
            new_b_1 = input('\t[%s]\nВведите жанр =>' % (field_1))
            new_b = '\''+str(new_b_1)+'\''
            setattr(self,field,eval(new_b))
            rt = rt+1
        elif field == 'author':
            while cb != 1:
                new_b_1 = input('\t[%s]\nВведите Фамилию, Имя,Отчество автора:' % (field_1))
                cb = protect_author(new_b_1)
                if cb == 1:
                    new_b = '\''+str(new_b_1)+'\''
                    setattr(self,field,eval(new_b))
                    rt = rt+1
                else: pass
        elif field == 'name':
            while cb != 1:
                new_b_1 = input('\t[%s]\nВведите название книги:' % (field_1))
                cb = protect_name(new_b_1)
                if cb == 1:
                    new_b = '\''+str(new_b_1)+'\''
                    setattr(self,field,eval(new_b))
                    rt = rt+1
                else: pass
    return self
