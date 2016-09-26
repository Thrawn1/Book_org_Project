import shelve
from m_vol_c import *
from s_vol_c import *
from new_book import *
from key_book_sort import *
from archive_short import *
def add_book_func(db_f):
        K1 = []
        for key in db_f:
                K1.append(key)
        if K1 == []:
                cv = 0
        else:
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
        print('\n\nЗапись занесена!')   
        print('\n\nПоследние 15 записей:')
        M = archive_short(1,1,db_f)
        d = len(M)
        vn = d - 15
        vn1 = d - 1
        J = M[vn:d:1]
        for key in J:
                n = db_f[key].voluminous
                h = db_f[key].accessory_type()
                if n == False:
                        print('\n','\t',db_f[key].author_name,db_f[key].author_middle_name,db_f[key].author_family,db_f[key].name_book,db_f[key].year_p,db_f[key].genre,h,('Полка №'+str(db_f[key].location)),'\n')
                elif n == True:
                        print('\n','\t',db_f[key].author_name,db_f[key].author_middle_name,db_f[key].author_family,db_f[key].name_book,db_f[key].year_p,db_f[key].genre,h,('Всего томов: '+str(db_f[key].total_vol)),('Номер тома: '+str(db_f[key].number_vol)),('Всего томов в библиотеке: '+str(db_f[key].availble_vol)),('Полка №'+str(db_f[key].location)),']','\n')
                else:
                       print('Ошибка определения многотмности')
        else: pass
        print('Всего записей в базе данных:',len(M))
        
        
# Данный модуль описывает добалвнеие новой записи в справочник. Принцип работы следуюший: Из базы данный выбираются все записи. Если в базе данных нет записей, некоторой переменной cv присваевается 0. Это нужно для того, что бы ключ в базе данных присваивался правильно.  Если записи в базе есть, происходит сортивровка ключей по кооэффициенту( от book0 -> book(n)).
#По скольку возможно удаление данных из базы данных, то предусмотрен механизм сортировки и прибавление 1 к последнему коээфициенту базы данных). В противном случае(если бы считалось общее количество записей), при удалении возникала бы ошибка присвоение коэффициента. 
#Итогом этих действий является перменная y, в которой содержится ключ новой, заносимой в базу данных, книги. 
#Далее происходит выбора типа добавляемой книги(Книга однотомная или двухтомная). Происходит вывод на экран вариантов и ожидание ввода с клавиатры одного из пунктов. Предусмотрена простейщая проверка на правильность введеного значения - программа выполняется дальше только в случае ввода 1 или 2. Во всех прочих случаях она выдает предупрежденрие. 
