from m_vol_c import *
from s_vol_c import *
from new_book import *
from key_book_sort import *
import shelve
def new_record(db_f):
    #Данная функция создает новую запись в БД
    K1 = []
    for key in db_f:
        K1.append(key)
    K = key_book_sort(K1)
    cv = int(K[len(K) -1].split('k')[1]) + 1
    y = 'book'+str(cv)
    print('\n\n\nВыберете, какой тип книги хотите добавить:\n\n1.Однотомная книга \n\n2.Многотомное собрание сочинений')
    type_in = input('\n\nВведите пункт меню:')
    if type_in == '1':
        j = S_vol()
        t = new_book(j)
    elif type_in =='2':
        j = M_vol()
        t = new_book(1,j)
    else:
        print('\nВведено не верное значение!')
    db_f[y]=t
    print('\nЗапись занесена!')
    return 1
