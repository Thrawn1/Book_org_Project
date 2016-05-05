from key_book_sort import *
def print_old_and_new_record(tmp_book,db_f,z1):
        h1 = db_f[z1].accessory_type()
        h2 = tmp_book.accessory_type()
        j = db_f[z1].voluminous_type()
        if j == 'Книга имеет один том':
                print('\n\n','\t','Старая запись',j,'[',db_f[z1].author_name,db_f[z1].author_middle_name,db_f[z1].author_family,db_f[z1].name_book,db_f[z1].year_p,db_f[z1].genre,h1,('Полка №'+str(db_f[z1].location)),']','\n')
                print('\n\n','\t','Новая запись',j,'[',tmp_book.author_name,tmp_book.author_middle_name,tmp_book.author_family,tmp_book.name_book,tmp_book.year_p,tmp_book.genre,h2,('Полка №'+str(tmp_book.location)),']','\n')
        elif j == 'Книга имеет несколько томов':
                print('\n\n','\t','Старая запись',j,'[',db_f[z1].author_name,db_f[z1].author_middle_name,db_f[z1].author_family,db_f[z1].name_book,db_f[z1].year_p,db_f[z1].genre,h1,('Всего томов: '+str(db_f[z1].total_vol)),('Номер тома: '+str(db_f[z1].number_vol)),('Всего томов в библиотеке: '+str(db_f[z1].availble_vol)),('Полка №'+str(db_f[z1].location)),']','\n')
                print('\n\n','\t','Новая запись',j,'[',tmp_book.author_name,tmp_book.author_middle_name,tmp_book.author_family,tmp_book.name_book,tmp_book.year_p,tmp_book.genre,h2,('Всего томов: '+str(tmp_book.total_vol)),('Номер тома: '+str(tmp_book.number_vol)),('Всего томов в библиотеке: '+str(tmp_book.availble_vol)),('Полка №'+str(tmp_book.location)),']','\n')
        else:
                print('Ошибка определения парметра многотмности')
def print_results_search(z,db_f):
        J =[]
        for cv in z:
                arc = db_f[cv].archive
                if arc == False:
                        J.append(cv)
                else:
                        pass
        z1 = key_book_sort(J)
        for key in z1:
                n = db_f[key].voluminous
                h = db_f[key].accessory_type()
                if n == False:
                        print('\n\n','\t',db_f[key].author_name,db_f[key].author_middle_name,db_f[key].author_family,db_f[key].name_book,db_f[key].year_p,db_f[key].genre,h,('Полка №'+str(db_f[key].location)),'\n')
                elif n == True:
                        print('\n\n','\t',db_f[key].author_name,db_f[key].author_middle_name,db_f[key].author_family,db_f[key].name_book,db_f[key].year_p,db_f[key].genre,h,('Всего томов: '+str(db_f[key].total_vol)),('Номер тома: '+str(db_f[key].number_vol)),('Всего томов в библиотеке: '+str(db_f[key].availble_vol)),('Полка №'+str(db_f[key].location)),']','\n')
                else:
                       print('Ошибка определения многотмности')
