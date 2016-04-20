import shelve
from protect_fields import *
from update_att_author import *
from accessory_definition import *
def update_for_key_att_m(db_f,z1,sm):
        tmp_book=db_f[z1]
        h1 = accessory_file(db_f,z1)
        if sm == True:
                sm1 = 'Книга имеет несколько томов'
        else:
                print('Ошибка определения атрибута многотомности')
        print('\n\n','\t',sm1,'[',db_f[z1].author,db_f[z1].name,db_f[z1].year_p,db_f[z1].genre,h1,('Всего томов: '+str(db_f[z1].total_vol)),('Номер тома: '+str(db_f[z1].number_vol)),('Всего томов в библиотеке: '+str(db_f[z1].availble_vol)),('Полка №'+str(db_f[z1].location)),']','\n')
        print('\n\nВыберете параметр записи, который вы хотите отредактировать:\n\n1.Отредактировать Фамилию Имя Отчество автора \n\n2.Отредактировать наименование книги\n\n3.Год издания книги\n\n4.Жанр книги\n\n5.Местоположение книги\n\n6.Чужая ли книга\n\n7.Всего томов в собрании\n\n8.Всего томов имеется в библиотеке\n\n9.Текущий номер тома\n\n')
        in22 = input('\nВведите пункт параметра записи: ')
        cb1 = 0
        if in22 == '1':
                pass
                #update_att_author(db_f,tmp_book,sm1,z1)
        elif in22 == '2':
                pass
                #update_att_name(db_f,tmp_book,sm1,z1)
        elif in22 == '3':
                pass
        elif in22 == '4':
                pass
        elif in22 == '5':
                pass
        elif in22 == '6':
                pass
        elif in22 == '7':
                pass
        elif in22 == '8':
                pass
        elif in22 == '9':
                pass
        else:
                print('Введите коректный номер параметра записи!')