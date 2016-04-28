from menu_all_search import *
from menu_update_from_key_att import *
import datetime
def update_from_search(in_2,db_f):
        R = []
        K = []
        n = menu_all_search(in_2,db_f)
        b = len(n)
        if b == 1:
                K.append(n[0])
                R.append(1)               
                in11 = '1'      
        elif b > 1:
                tmp = 1
                tmp1 = 0
                for key in n:
                        K.append(key)
                        R.append(tmp)
                        tmp = tmp + 1
                K1 = key_book_sort(K)
                for b in K1:
                        num1 = R[tmp1]
                        n = db_f[b].voluminous
                        h = accessory_file (db_f,b)
                        if n == False:
                                print('\n','\t',num1,'.','   [',db_f[b].author,db_f[b].name,db_f[b].year_p,db_f[b].genre,h,('Полка №'+str(db_f[b].location)),']','\n')
                        elif n == True:
                                print('\n','\t',num1,'.','   [',db_f[b].author,db_f[b].name,db_f[b].year_p,db_f[b].genre,h,('Всего томов: '+str(db_f[b].total_vol)),('Номер тома: '+str(db_f[b].number_vol)),('Всего томов в библиотеке: '+str(db_f[b].availble_vol)),('Полка №'+str(db_f[b].location)),']','\n')
                        else:
                                print('Ошибка определения многотмности')
                        tmp1 = tmp1 + 1 
                in11 = input('Введите ключ записи, которую хотите отредактировать: ')
        else:
                print('Ничего не найдено!')
        v = menu_update_from_key_att(db_f,in11,R,K)
        v1 = v[0]
        v2 = v[1]
        time = datetime.datetime.now()
        date_str = time.strftime("%d-%m-%Y")
        d = '\''+ date_str + '\''
        setattr(v1,'data_last_editing',eval(d))
        db_f[v2] = v1
        db_f.close()
