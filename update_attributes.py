import shelve
from accessory_definition import *
from voluminous_book import *
from protect_fields import *
from print_results import *
def update_att_author(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Автор книги')
        kj = db_f[z1].author
        print('\n\nСтарое значение: ', kj)
        while cb1 != 1:
                new_b_1 = input('\t[%s]\nВведите Фамилию, Имя,Отчество автора: ' % (field_1))
                cb1 = protect_author(new_b_1)
                if cb1 == 1:
                        new_b = '\''+str(new_b_1)+'\''
                        setattr(tmp_book,'author',eval(new_b))
                        print_old_and_new_record(tmp_book,db_f,z1)
                        return tmp_book
def update_att_name(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Название книги')
        kj = db_f[z1].name
        print('\n\nСтарое значение: ', kj)
        while cb1 != 1:
                new_b_1 = input('\t[%s]\nВведите название книги: ' % (field_1))
                cb1 = protect_author(new_b_1)
                if cb1 == 1:
                        new_b = '\''+str(new_b_1)+'\''
                        setattr(tmp_book,'name',eval(new_b))
                        print_old_and_new_record(tmp_book,db_f,z1)
                        return tmp_book
def update_att_year_p(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Год издания')
        kj = db_f[z1].year_p
        print('\n\nСтарое значение: ', kj,'год')
        while cb1 != 1:
                new_b_1 = input('\t[%s]\nГод издания:' % (field_1))
                cb1 = protect_author(new_b_1)
                if cb1 == 1:
                        setattr(tmp_book,'year_p',eval(new_b_1))
                        print_old_and_new_record(tmp_book,db_f,z1)
                        return tmp_book
def update_att_genre(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Жанр')
        kj = db_f[z1].genre
        print('\n\nСтарое значение: ', kj)
        while cb1 != 1:
                new_b_1 = input('\t[%s]\nВведите Жанр:' % (field_1))
                cb1 = protect_author(new_b_1)
                if cb1 == 1:
                        new_b = '\''+str(new_b_1)+'\''
                        setattr(tmp_book,'genre',eval(new_b))
                        print_old_and_new_record(tmp_book,db_f,z1)
                        return tmp_book
def update_att_location(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Где расположена книга')
        kj = db_f[z1].location
        print('\n\nСтарое значение: ','Полка №', kj)
        while cb1 != 1:
                new_b_1 = input('\t[%s]\nВведите № полки на которой находится книга: ' % (field_1))
                cb1 = protect_author(new_b_1)
                if cb1 == 1:
                        setattr(tmp_book,'location',eval(new_b))
                        print_old_and_new_record(tmp_book,db_f,z1)
                        return tmp_book
def update_att_accessory(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Чужая ли книга?')
        h1 = accessory_file(db_f,z1)
        print('\n\nСтарое значение: ', h1)
        while cb1 != 1:
                print('Пожалуйста выберете один из вариантов:\n1. Книга ваша\n2. Книга чужая')
                new_b_1 = input('\t[%s]\n :' % (field_1))
                if new_b_1 == '1':
                        cvv = False
                        cb1 = 1
                elif new_b_1 == '2':
                        cvv = True
                        cb1 = 1
                else:
                        print('Ошибка! Выберет один из двух вариантов')
                        cb1 = 0
                setattr(tmp_book,'accessory',cvv)
                print_old_and_new_record(tmp_book,db_f,z1)
                return tmp_book
def update_att_total_vol(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Всего томов в собрании')
        kj = db_f[z1].total_vol
        print('\n\nСтарое значение: ', kj,' томов')
        while cb1 != 1:
                new_b_1 = input('\t[%s]\nВведите количество томов в собрании:' % (field_1))
                cb1 = protect_total_vol(new_b_1)
                if cb1 == 1:
                        setattr(tmp_book,'total_vol',eval(new_b))
                        print_old_and_new_record(tmp_book,db_f,z1)
                        return tmp_book
def update_att_number_vol(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Номер тома')
        kj = db_f[z1].number_vol
        print('\n\nСтарое значение: ','Том №', kj)
        while cb1 != 1:
                new_b_1 = input('\t[%s]\nВведите Номер тома:' % (field_1))
                cb1 = protect_total_vol(new_b_1)
                if cb1 == 1:
                        setattr(tmp_book,'number_vol',eval(new_b))
                        print_old_and_new_record(tmp_book,db_f,z1)
                        return tmp_book                       
def update_att_availble_vol(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Имеющиеся в наличии количество томов')
        kj = db_f[z1].availble_vol
        print('\n\nСтарое значение: ','имеется томов - ', kj)
        while cb1 != 1:
                new_b_1 = input('\t[%s]\nВведите количество томов, которые имеются в наличии:' % (field_1))
                cb1 = protect_total_vol(new_b_1)
                if cb1 == 1:
                        setattr(tmp_book,'availble_vol',eval(new_b))
                        print_old_and_new_record(tmp_book,db_f,z1)
                        return tmp_book
