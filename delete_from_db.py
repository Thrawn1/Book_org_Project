import shelve
from archive_short import *
def delete_from_db (db_f):
        password = input('\n\nВведите пароль: ')
        if password == '12':
                K1 = archive_short(2,3,db_f)
                for b in K1:
                        h = db_f[b].accessory_type()
                        j = db_f[b].voluminous_type()
                        if j == 'Книга имеет один том':
                                print('\n\n','\t','[',b,']',j,'[',db_f[b].author_name,db_f[b].author_middle_name,db_f[b].author_family,db_f[b].name_book,db_f[b].year_p,db_f[b].genre,h,('Полка №'+str(db_f[b].location)),']','\n')
                        elif j == 'Книга имеет несколько томов':
                                print('\n\n','\t','[',b,']',j,'[',db_f[b].author_name,db_f[b].author_middle_name,db_f[b].author_family,db_f[b].name_book,db_f[b].year_p,db_f[b].genre,h,('Всего томов: '+str(db_f[b].total_vol)),('Номер тома: '+str(db_f[b].number_vol)),('Всего томов в библиотеке: '+str(db_f[b].availble_vol)),('Полка №'+str(db_f[b].location)),']','\n')
                        else:
                                print('Ошибка определения парметра многотмности')
                u = input('Введите ключ: ')
                del db_f[u]
                print('Запись с ключом',u,'удалена безвозвратно!')
        else:
                print('\n\n\tВведен не верный пароль. Для удаления обратитесь к администратору!\n\n\n')
        
