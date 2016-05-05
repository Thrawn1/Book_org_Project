import shelve
from protect_fields import *
from print_results import *
def update_att_author(db_f,tmp_book,z1):
        kj = str(db_f[z1].author_name) +' '+ str(db_f[z1].author_middle_name) + ' ' + str(db_f[z1].author_family)
        nnn = 9
        while nnn != 1:
                print('\n\nСтарое значение: ', kj)        
                print('\n\nВыберете, что вы хотите отредактировать:\n\n\t1. Имя автора\n\n\t2. Отчество автора\n\n\t3. Фамилию автора')
                in10 = input('\n\n\nВведите пункт меню: ')
                if in10 == '1':
                        field_1 = ('Имя автора книги')
                        cb1 = 0
                        while cb1 != 1:
                                new_b_1 = input('\t[%s]\nВведите имя автора: ' % (field_1))
                                cb1 = protect_author(new_b_1)
                                if cb1 == 1:
                                        setattr(tmp_book,'author_name',new_b_1)
                                        print_old_and_new_record(tmp_book,db_f,z1)
                                        print('Вы хотите отредактировать автора еще? Да/Нет')
                                        mmm = 1
                                        while mmm != 0:
                                                jk = input('Введите подверждение:')
                                                jk1 = jk.lower()
                                                if jk1 == 'да' or jk1 == 'yes' or jk1 == 'y' or jk1 =='д':
                                                        nnn = 2
                                                        mmm = 0
                                                elif jk1 == 'нет' or jk1 == 'no' or jk1 == 'н' or jk1 =='n':
                                                        nnn = 1
                                                        return tmp_book
                                                        mmm = 0
                                                else:
                                                        print('Введите нормальное подверждение!')
                                                        mmm = 1
                elif in10 == '2':
                        field_1 = ('Отчество автора книги')
                        cb1 = 0
                        while cb1 != 1:
                                new_b_1 = input('\t[%s]\nВведите отчество автора: ' % (field_1))
                                cb1 = protect_author(new_b_1)
                                if cb1 == 1:
                                        setattr(tmp_book,'author_middle_name',new_b_1)
                                        print_old_and_new_record(tmp_book,db_f,z1)
                                        print('Вы хотите отредактировать автора еще? Да/Нет')
                                        mmm = 1
                                        while mmm != 0:
                                                jk = input('Введите подверждение:')
                                                jk1 = jk.lower()
                                                if jk1 == 'да' or jk1 == 'yes' or jk1 == 'y' or jk1 =='д':
                                                        nnn = 2
                                                        mmm = 0
                                                elif jk1 == 'нет' or jk1 == 'no' or jk1 == 'н' or jk1 =='n':
                                                        nnn = 1
                                                        return tmp_book
                                                        mmm = 0
                                                else:
                                                        print('Введите нормальное подверждение!')
                                                        mmm = 1
                elif in10 == '3':
                        field_1 = ('Фамилия автора книги')
                        cb1 = 0
                        while cb1 != 1:
                                new_b_1 = input('\t[%s]\nВведите фамилию автора: ' % (field_1))
                                cb1 = protect_author(new_b_1)
                                if cb1 == 1:
                                        setattr(tmp_book,'author_family',new_b_1)
                                        print_old_and_new_record(tmp_book,db_f,z1)
                                        print('Вы хотите отредактировать автора еще? Да/Нет')
                                        mmm = 1
                                        while mmm != 0:
                                                jk = input('Введите подверждение:')
                                                jk1 = jk.lower()
                                                if jk1 == 'да' or jk1 == 'yes' or jk1 == 'y' or jk1 =='д':
                                                        nnn = 2
                                                        mmm = 0
                                                elif jk1 == 'нет' or jk1 == 'no' or jk1 == 'н' or jk1 =='n':
                                                        nnn = 1
                                                        return tmp_book
                                                        mmm = 0
                                                else:
                                                        print('Введите нормальное подверждение!')
                                                        mmm = 1
                else:
                        print('Выбрано недопустимое значение!')
        
        
def update_att_name_book(db_f,tmp_book,z1):
        cb1 = 0
        field_1 = ('Название книги')
        kj = db_f[z1].name_book
        print('\n\nСтарое значение: ', kj)
        while cb1 != 1:
                new_b_1 = input('\t[%s]\nВведите название книги: ' % (field_1))
                cb1 = protect_author(new_b_1)
                if cb1 == 1:
                        setattr(tmp_book,'name_book',new_b_1)
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
                        setattr(tmp_book,'year_p',new_b_1)
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
                        setattr(tmp_book,'genre',new_b_1)
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
                        setattr(tmp_book,'location',new_b_1)
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
                        setattr(tmp_book,'total_vol',new_b_1)
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
                        setattr(tmp_book,'number_vol',new_b_1)
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
                        setattr(tmp_book,'availble_vol',new_b_1)
                        print_old_and_new_record(tmp_book,db_f,z1)
                        return tmp_book
