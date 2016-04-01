#! /usr/bin/env python
# -*- coding: utf-8 -*-
from m_vol_c import *
from protect_fields import *
def multi_book():
    t = M_vol()
    fieldnmes = ('author','name','year_p','genre','location','accessory','total_vol','number_vol','availble_vol')
    fieldnmes_1 = ('Автор книги','Название книги','Год издания','Жанр','Где расположена книга','Чужая ли книга?','Всего томов?','Номер тома','Всего томов есть в наличии')
    rt = 0
    for field in fieldnmes:
        cb = 0
        field_1 = fieldnmes_1[rt]
        if field == 'year_p':
            while cb != 1:
                new_b = input('\t[%s]\nВведите год издания:' % (field_1))
                cb = protect_date(new_b)
                if cb == 1:
                    setattr(t,field,eval(new_b))
                    rt = rt+1
                else: pass
        elif field == 'location':
            while cb != 1:
                new_b = input('\t[%s]\nВведите номер полки:' % (field_1))
                cb = protect_location(new_b)
                if cb == 1:
                    setattr(t,field,eval(new_b))
                    rt = rt+1
                else: pass
        elif field == 'accessory':
            print('Пожалуйста выберете один из вариантов:\n1. Книга ваша\n2. Книга чужая')
            new_b = int(input('\t[%s]\n:' % (field_1)))
            if new_b == 1:
                setattr(t,field,False)
                rt = rt+1
            elif new_b == 2:
                setattr(t,field,True)
                rt = rt+1
            else:
                print('Выбрано недопустимое значение!')
        elif field == 'genre':
            new_b_1 = input('\t[%s]\nВведите жанр =>' % (field_1))
            new_b = '\''+str(new_b_1)+'\''
            setattr(t,field,eval(new_b))
            rt = rt+1
        elif field == 'author':
            while cb != 1:
                new_b_1 = input('\t[%s]\nВведите Фамилию, Имя,Отчество автора:' % (field_1))
                cb = protect_author(new_b_1)
                if cb == 1:
                    new_b = '\''+str(new_b_1)+'\''
                    setattr(t,field,eval(new_b))
                    rt = rt+1
                else: pass
        elif field == 'name':
            while cb != 1:
                new_b_1 = input('\t[%s]\nВведите название книги:' % (field_1))
                cb = protect_name(new_b_1)
                if cb == 1:
                    new_b = '\''+str(new_b_1)+'\''
                    setattr(t,field,eval(new_b))
                    rt = rt+1
                else: pass
        elif field == 'total_vol':
            while cb != 1:
                new_b = input('\t[%s]\nВведите общее количество томов в собрании:' % (field_1))
                cb = protect_total_vol(new_b)
                if cb == 1:
                    setattr(t,field,eval(new_b))
                    rt = rt+1
                else: pass
        elif field == 'number_vol':
            while cb != 1:
                new_b = input('\t[%s]\nВведите номер тома:' % (field_1))
                cb = protect_total_vol(new_b)
                if cb == 1:
                    setattr(t,field,eval(new_b))
                    rt = rt+1
                else: pass
        elif field == 'availble_vol':
            while cb != 1:
                new_b = input('\t[%s]\nВведите  количество томов в наличии:' % (field_1))
                cb = protect_total_vol(new_b)
                if cb == 1:
                    setattr(t,field,eval(new_b))
                    rt = rt+1
                else: pass
    return t