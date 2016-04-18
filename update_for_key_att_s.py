import shelve
from protect_fields import *
def update_for_key_att_s(db_f,z1,sm):
        h = db_f[z1].accessory
        if h == False:
                h1 = 'Книга своя'
        else:
                h1 = 'Книга чужая'
        if sm == False:
                sm1 = 'Книга не имеет томов'
        else:
                print('Ошибка определения атрибута многотомности')
        print('\n\n','\t',sm1,'[',db_f[z1].author,db_f[z1].name,db_f[z1].year_p,('Полка №'+str(db_f[z1].location)),db_f[z1].genre,h1,']','\n')
        print('\n\nВыберете параметр записи, который вы хотите отредактировать:\n\n1.Отредактировать Фамилию Имя Отчество \n\n2.Отредактировать наименование книги\n\n3.Год издания\n\n4.Жанр\n\n5.Местоположение\n\n6.Чужая ли книга\n\n')
        in22 = input('\nВведите пункт параметра записи: ')
        cb1 = 0
        if in22 == '1':
                field_1 = ('Автор книги')
                kj = db_f[z1].author
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите Фамилию, Имя,Отчество автора: ' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
#new_b = '\''+str(new_b_1)+'\''
#setattr(self,field,eval(new_b))
#rt = rt+1
# else: pass
        elif in22 == '2':
                field_1 = ('Название книги')
                kj = db_f[z1].name
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите название книги: ' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '3':
                field_1 = ('Год издания')
                kj = db_f[z1].year_p
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите год издания: ' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '4':
                field_1 = ('Жанр')
                kj = db_f[z1].genre
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите Жанр: ' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '5':
                field_1 = ('Где расположена книга')
                kj = db_f[z1].location
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите № полки на которой находится книга: ' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '6':
                field_1 = ('Чужая ли книга?')
                kj = db_f[z1].accessory
                if kj == False:
                    gh = 'Книга ваша'
                elif kj == True:
                    gh = 'Книга чужая'
                else:
                    print('Ошибка определения принадлежности книги!')
                print('\n\nСтарое значение: ', gh)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\n :' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        else:
                print('Введите коректный номер параметра записи!')
