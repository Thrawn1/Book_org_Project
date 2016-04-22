from voluminous_book import *
from accessory_definition import *
def print_old_and_new_record(tmp_book,db_f,z1):
        h1 = accessory_file (db_f,z1)
        h2 = accessory_class(tmp_book)
        j = voluminous_book(db_f,z1)
        if j == 'Книга имеет один том':
                print('\n\n','\t','Старая запись',j,'[',db_f[z1].author,db_f[z1].name,db_f[z1].year_p,db_f[z1].genre,h1,('Полка №'+str(db_f[z1].location)),']','\n')
                print('\n\n','\t','Новая запись',j,'[',tmp_book.author,tmp_book.name,tmp_book.year_p,tmp_book.genre,h2,('Полка №'+str(tmp_book.location)),']','\n')
        elif j == 'Книга имеет несколько томов':
                print('\n\n','\t','Старая запись',j,'[',db_f[z1].author,db_f[z1].name,db_f[z1].year_p,db_f[z1].genre,h1,('Всего томов: '+str(db_f[z1].total_vol)),('Номер тома: '+str(db_f[z1].number_vol)),('Всего томов в библиотеке: '+str(db_f[z1].availble_vol)),('Полка №'+str(db_f[z1].location)),']','\n')
                print('\n\n','\t','Новая запись',j,'[',tmp_book.author,tmp_book.name,tmp_book.year_p,tmp_book.genre,h2,('Всего томов: '+str(tmp_book.total_vol)),('Номер тома: '+str(tmp_book.number_vol)),('Всего томов в библиотеке: '+str(tmp_book.availble_vol)),('Полка №'+str(tmp_book.location)),']','\n')
        else:
                print('Ошибка определения парметра многотмности')
def print_results_search(z):
        for key in z:
                print('\n','\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')