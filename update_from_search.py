from menu_all_search import *
from menu_update_from_key_att import *
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
                for b in K:
                        num1 = R[tmp1]
                        print('\n','\t',num1,': ',db_f[b].author,db_f[b].name,db_f[b].year_p,('Полка №'+str(db_f[b].location)),'\n')
                        tmp1 = tmp1 + 1 
                in11 = input('Введите ключ записи, которую хотите отредактировать: ')
        else:
                print('Ничего не найдено!')
        v = menu_update_from_key_att(db_f,in11,R,K)
        v1 = v[0]
        v2 = v[1]
        db_f[v2] = v1
        db_f.close()
