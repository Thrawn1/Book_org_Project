import shelve
from m_vol_c import *
from s_vol_c import *
from new_record_s import *
from new_record_m import *
from key_book_sort import *
def add_book_func(db_f):
#Данная функция была объявлена для удобства - теперь в menu.py все логично - формируется только меню и вызываются нужные функции, а не как раньше - добавление записи БД
# Возможно стоит переработать функцию new_record, и объединить с этой, что бы не усложнять проект
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
                t = single_book(j)
        elif type_in =='2':
                j = M_vol()
                t1 = single_book(j)
                t = multi_book(t1)
        else:
                print('\nВведено не верное значение!')
        db_f[y]=t
        print('\nЗапись занесена!')   

        K2=[]
        print('Последние 15 записей:')
        for key in db_f:
                K2.append(key)
        M = key_book_sort(K2)
        d = len(M)
        vn = d - 15
        vn1 = d - 1
        J = M[vn:d:1]
        print(d,vn,vn1)
        print(J)
        for key in J:
                print('\t',key,db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
        else: pass
        print('Всего записей в базе данных:',len(M))
