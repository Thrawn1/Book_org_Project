from archive_short import *
def list_archive_book(db_f):
        K1 = archive_short(1,2,db_f)
        for b in K1:
                n = db_f[b].voluminous
                h = db_f[b].accessory_type()
                if n == False:
                        print('\n','\t','[',db_f[b].author_name,db_f[b].author_middle_name,db_f[b].author_family,db_f[b].name_book,db_f[b].year_p,db_f[b].genre,h,('Полка №'+str(db_f[b].location)),'Дата перехода книги в архив: ',db_f[b].data_archive,'Комменатрий к удалению в ахрив: ',db_f[b].comment_archive,']','\n ')
                elif n == True:
                        print('\n','\t','[',db_f[b].author_name,db_f[b].author_middle_name,db_f[b].author_family,db_f[b].name_book,db_f[b].year_p,db_f[b].genre,h,('Всего томов: '+str(db_f[b].total_vol)),('Номер тома: '+str(db_f[b].number_vol)),('Всего томов в библиотеке: '+str(db_f[b].availble_vol)),('Полка №'+str(db_f[b].location)),'Дата перехода книги в архив: ',db_f[b].data_archive,'Комменатрий к удалению в ахрив: ',db_f[b].comment_archive,']','\n')
                else:
                        print('Ошибка определения многотмности')
                
