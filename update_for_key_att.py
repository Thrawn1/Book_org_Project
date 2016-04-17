import shelve
from protect_fields import *
def update_for_key_att(db_f,R,K):
        pass
        in11 = input('Введите ключ записи, которую хотите отредактировать: ')
        y = int(in11) in R
        z = int(in11) - 1
        if y == True and z >= 0:
                z1 = K[z]
                h = db_f[z1].accessory
                if h == False:
                        h1 = 'Книга своя'
                else:
                        h1 = 'Книга чужая'
                print('\n\n','\t','[',db_f[z1].author,db_f[z1].name,db_f[z1].year_p,('Полка №'+str(db_f[z1].location)),db_f[z1].genre,h1,']','\n')
                print('\n\nВыберете параметр записи, который вы хотите отредактировать:\n\n1.Отредактировать Фамилию Имя Отчество \n\n2.Отредактировать наименование книги\n\n3.Год издания\n\n4.Жанр\n\n5.Местоположение\n\n6.Чужая ли книга\n\n7.Всего томов в собрании*(будет доработано для многотомных книг)\n\n8.Всего томов имеется в библиотеке*(будет доработано для многотомных книг)\n\n9.Текущий номер тома*(будет доработано для многотомных книг)\n\n')
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
                        pass
                        field_1 = ('Название книги')
                        kj = db_f[z1].name
                        print('\n\nСтарое значение: ', kj)
                        while cb1 != 1:
                                new_b_1 = input('\t[%s]\nВведите название книги: ' % (field_1))
                                cb1 = protect_author(new_b_1)
                                if cb1 == 1:
                                        print('Yes!')
                elif in22 == '3':
                        pass
                        field_1 = ('Год издания')
                        kj = db_f[z1].year_p
                        print('\n\nСтарое значение: ', kj)
                        while cb1 != 1:
                                new_b_1 = input('\t[%s]\nВведите Фамилию, Имя,Отчество автора:' % (field_1))
                                cb1 = protect_author(new_b_1)
                                if cb1 == 1:
                                        print('Yes!')
                elif in22 == '4':
                        pass
                        field_1 = ('Жанр')
                        kj = db_f[z1].genre
                        print('\n\nСтарое значение: ', kj)
                        while cb1 != 1:
                                new_b_1 = input('\t[%s]\nВведите Фамилию, Имя,Отчество автора:' % (field_1))
                                cb1 = protect_author(new_b_1)
                                if cb1 == 1:
                                        print('Yes!')
                elif in22 == '5':
                        pass
                        field_1 = ('Где расположена книга')
                        kj = db_f[z1].location
                        print('\n\nСтарое значение: ', kj)
                        while cb1 != 1:
                                new_b_1 = input('\t[%s]\nВведите Фамилию, Имя,Отчество автора:' % (field_1))
                                cb1 = protect_author(new_b_1)
                                if cb1 == 1:
                                        print('Yes!')
                elif in22 == '6':
                        pass
                        field_1 = ('Чужая ли книга?')
                        kj = db_f[z1].accessory
                        print('\n\nСтарое значение: ', kj)
                        while cb1 != 1:
                                new_b_1 = input('\t[%s]\nВведите Фамилию, Имя,Отчество автора:' % (field_1))
                                cb1 = protect_author(new_b_1)
                                if cb1 == 1:
                                        print('Yes!')
                elif in22 == '7':
                        pass 
                elif in22 == '8':
                        pass
                elif in22 == '9':
                        pass
                else:
                        print('Введите коректный номер параметра записи!')
        else:
                print('Введите корректный номер записи!')
