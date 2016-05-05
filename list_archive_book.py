from key_book_sort import *
def list_archive_book(db_f):
        R = []
        for key in db_f:
                uu = db_f[key].archive 
                if uu == True:
                        R.append(key)
                else:
                        pass
        K1 = key_book_sort(R)
        for b in K1:
                n = db_f[b].voluminous
                h = db_f[b].accessory_type()
                if n == False:
                        print('\n','\t','[',db_f[b].author_name,db_f[b].author_middle_name,db_f[b].author_family,db_f[b].name_book,db_f[b].year_p,db_f[b].genre,h,('Полка №'+str(db_f[b].location)),'Дата перехода книги в архив: ',db_f[b].data_archive,'Комменатрий к удалению в ахрив: ',db_f[b].comment_archive,']','\n ')
                elif n == True:
                        print('\n','\t','[',db_f[b].author_name,db_f[b].author_middle_name,db_f[b].author_family,db_f[b].name_book,db_f[b].year_p,db_f[b].genre,h,('Всего томов: '+str(db_f[b].total_vol)),('Номер тома: '+str(db_f[b].number_vol)),('Всего томов в библиотеке: '+str(db_f[b].availble_vol)),('Полка №'+str(db_f[b].location)),'Дата перехода книги в архив: ',db_f[b].data_archive,'Комменатрий к удалению в ахрив: ',db_f[b].comment_archive,']','\n')
                else:
                        print('Ошибка определения многотмности')
                
