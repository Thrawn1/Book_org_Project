import shelve
from key_book_sort import *
from accessory_definition import *
from voluminous_book import *
def delete_from_db (db_f):
        password = input('\n\nВведите пароль: ')
        if password == '12':
                K = []
                for key in db_f:
                        K.append(key)
                K1 = key_book_sort(K)
                for b in K1:
                        h = accessory_file (db_f,b)
                        j = voluminous_book(db_f,b)
                        if j == 'Книга имеет один том':
                                print('\n\n','\t','[',b,']',j,'[',db_f[b].author,db_f[b].name,db_f[b].year_p,db_f[b].genre,h,('Полка №'+str(db_f[b].location)),']','\n')
                        elif j == 'Книга имеет несколько томов':
                                print('\n\n','\t','[',b,']',j,'[',db_f[b].author,db_f[b].name,db_f[b].year_p,db_f[b].genre,h,('Всего томов: '+str(db_f[b].total_vol)),('Номер тома: '+str(db_f[b].number_vol)),('Всего томов в библиотеке: '+str(db_f[b].availble_vol)),('Полка №'+str(db_f[b].location)),']','\n')
                        else:
                                print('Ошибка определения парметра многотмности')
                u = input('Введите ключ: ')
                del db_f[u]
                print('Запись с ключом',u,'удалена безвозвратно!')
        else:
                print('\n\n\tВведен не верный пароль. Для удаления обратитесь к администратору!\n\n\n')
        
