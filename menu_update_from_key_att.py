import shelve
from update_attributes import *
def menu_update_from_key_att(db_f,in11,R,K):
        y = int(in11) in R
        z = int(in11) - 1
        if y == True and z >= 0:
                z1 = K[z]
                tmp_book = db_f[z1]
                h1 = db_f[z1].accessory_type()
                sm1 = db_f[z1].voluminous_type()
                if sm1 == 'Книга имеет один том':
                        print('\n\n','\t',sm1,'[',db_f[z1].author_name,db_f[z1].author_middle_name,db_f[z1].author_family,db_f[z1].name_book,db_f[z1].year_p,db_f[z1].genre,h1,('Полка №'+str(db_f[z1].location)),']','\n')
                        print('\n\nВыберете параметр записи, который вы хотите отредактировать:\n\n1.Отредактировать Фамилию Имя Отчество автора \n\n2.Отредактировать наименование книги\n\n3.Год издания книги\n\n4.Жанр книги\n\n5.Местоположение книги\n\n6.Чужая ли книга\n\n')
                        in22 = input('\nВведите пункт параметра записи: ')
                        cb1 = 0
                        if in22 == '1':
                                update_att_author(db_f,tmp_book,z1)
                        elif in22 == '2':
                                update_att_name_book(db_f,tmp_book,z1)
                        elif in22 == '3':
                                update_att_year_p(db_f,tmp_book,z1)
                        elif in22 == '4':
                                update_att_genre(db_f,tmp_book,z1)
                        elif in22 == '5':
                                update_att_location(db_f,tmp_book,z1)
                        elif in22 == '6':
                                update_att_accessory(db_f,tmp_book,z1)
                        else:
                                print('Введите коректный номер параметра записи!')
                elif sm1 == 'Книга имеет несколько томов':
                        print('\n\n','\t',sm1,'[',db_f[z1].author_name,db_f[z1].author_middle_name,db_f[z1].author_family,db_f[z1].name_book,db_f[z1].year_p,db_f[z1].genre,h1,('Всего томов: '+str(db_f[z1].total_vol)),('Номер тома: '+str(db_f[z1].number_vol)),('Всего томов в библиотеке: '+str(db_f[z1].availble_vol)),('Полка №'+str(db_f[z1].location)),']','\n')
                        print('\n\nВыберете параметр записи, который вы хотите отредактировать:\n\n1.Отредактировать Фамилию Имя Отчество автора \n\n2.Отредактировать наименование книги\n\n3.Год издания книги\n\n4.Жанр книги\n\n5.Местоположение книги\n\n6.Чужая ли книга\n\n7.Всего томов в собрании\n\n8.Всего томов имеется в библиотеке\n\n9.Текущий номер тома\n\n')
                        in22 = input('\nВведите пункт параметра записи: ')
                        cb1 = 0
                        if in22 == '1':
                                update_att_author(db_f,tmp_book,z1)
                        elif in22 == '2':
                                update_att_name_book(db_f,tmp_book,z1)
                        elif in22 == '3':
                                update_att_year_p(db_f,tmp_book,z1)
                        elif in22 == '4':
                                update_att_genre(db_f,tmp_book,z1)
                        elif in22 == '5':
                                update_att_location(db_f,tmp_book,z1)
                        elif in22 == '6':
                                update_att_accessory(db_f,tmp_book,z1)
                        elif in22 == '7':
                                update_att_total_vol(db_f,tmp_book,z1)
                        elif in22 == '8':
                                update_att_number_vol(db_f,tmp_book,z1)
                        elif in22 == '9':
                                update_att_availble_vol(db_f,tmp_book,z1)
                        else:
                                print('Введите коректный номер параметра записи!')
                else: pass
                return tmp_book, z1         
        else:
                print('Введите корректный номер записи!')
