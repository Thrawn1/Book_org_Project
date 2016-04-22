import shelve
from menu_update_from_key_att import *
def update_for_key():
        K = []
        R = []
        tmp = 1
        tmp1 = 0
        db_f = shelve.open('book_db_2')
        for key in db_f:
                K.append(key)
                R.append(tmp)
                tmp = tmp + 1
        for b in K:
                num1 = R[tmp1]
                print('\n','\t',num1,': ',db_f[b].author,db_f[b].name,db_f[b].year_p,('Полка №'+str(db_f[b].location)),'\n')
                tmp1 = tmp1 + 1 
        in11 = input('Введите ключ записи, которую хотите отредактировать: ')
        v = menu_update_from_key_att(db_f,in11,R,K)
        v1 = v[0]
        v2 = v[1]
        db_f[v2] = v1
        db_f.close()