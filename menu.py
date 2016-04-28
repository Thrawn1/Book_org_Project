from menu_all_search import *
from menu_update import *
from print_results import *
from add_book_func import *
from menu_delete import *
from key_book_sort import *
def menu (db_f):
        print('\n\n\tВыберете действие:\n\n\n1.Внеcение записи в базу данных\n\n2.Поиск книг в базе данных\n\n3.Изменение в записи базы данных\n\n4.Удаление записи из базы данных')
        in00 = input('\n\nВведите нужны пункт меню:')
        if in00 == '1':
                add_book_func(db_f)
        elif in00 =='2':
                in_2 = input('\n\nВведите количество резульатов поиска,отображаемых на экране: ')
                z = menu_all_search(in_2,db_f)
                print_results_search(z,db_f)
        elif in00 =='3':
                menu_update(db_f)
        elif in00 =='4':
                menu_delete(db_f)
        elif in00 == '5':
                R = []
                K = []
                tmp = 1
                tmp1 = 0
                for key in db_f:
                        R.append(key)
                        K.append(tmp)
                        tmp = tmp+1
                K1 = key_book_sort(R)
                for b in K1:
                        num1 = K[tmp1]
                        print('\n','\t',num1,': ',[b],db_f[b].author,db_f[b].name,db_f[b].year_p,('Полка №'+str(db_f[b].location)),db_f[b].data_creating,db_f[b].data_last_editing,db_f[b].data_archive,'\n')
                        tmp1 = tmp1 + 1
        else: 
                print ('\n\nВведен не верный пункт меню или не допустимое значение!')
