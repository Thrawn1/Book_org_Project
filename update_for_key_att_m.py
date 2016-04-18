import shelve
from protect_fields import *
def update_for_key_att_m(db_f,z1,sm):
        h = db_f[z1].accessory
        if h == False:
                h1 = 'Книга своя'
        else:
                h1 = 'Книга чужая'
        if sm == False:
                sm1 = 'Книга имеет несколько томов'
        else:
                print('Ошибка определения атрибута многотомности')
        print('\n\n','\t',sm1,'[',db_f[z1].author,db_f[z1].name,db_f[z1].year_p,db_f[z1].genre,h1,('Всего томов: '+str(db_f[z1].total_vol)),('Номер тома: '+str(db_f[z1].number_vol)),('Всего томов в библиотеке: '+str(db_f[z1].availble_vol)),('Полка №'+str(db_f[z1].location)),']','\n')
        print('\n\nВыберете параметр записи, который вы хотите отредактировать:\n\n1.Отредактировать Фамилию Имя Отчество \n\n2.Отредактировать наименование книги\n\n3.Год издания\n\n4.Жанр\n\n5.Местоположение\n\n6.Чужая ли книга\n\n7.Всего томов в собрании\n\n8.Всего томов имеется в библиотеке\n\n9.Текущий номер тома\n\n')
        in22 = input('\nВведите пункт параметра записи: ')
        cb1 = 0
        if in22 == '1':
                pass
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
                        new_b_1 = input('\t[%s]\nГод издания:' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '4':
                pass
                field_1 = ('Жанр')
                kj = db_f[z1].genre
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите Жанр:' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '5':
                pass
                field_1 = ('Где расположена книга')
                kj = db_f[z1].location
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите № полки на которой находится книга: ' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '6':
                pass
                field_1 = ('Чужая ли книга?')
                kj = db_f[z1].accessory
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\n :' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '7':
                field_1 = ('Всего томов в собрании')
                kj = db_f[z1].accessory
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите количество томов в собрании:' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '8':
                field_1 = ('Номер тома')
                kj = db_f[z1].accessory
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите Номер тома:' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        elif in22 == '9':
                field_1 = ('Имеющиеся в наличии количество томов')
                kj = db_f[z1].accessory
                print('\n\nСтарое значение: ', kj)
                while cb1 != 1:
                        new_b_1 = input('\t[%s]\nВведите количество томов, которые имеются в наличии:' % (field_1))
                        cb1 = protect_author(new_b_1)
                        if cb1 == 1:
                                print('Yes!')
        else:
                print('Введите коректный номер параметра записи!')
