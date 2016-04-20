import shelve
from update_for_key_att_m import *
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
        y = int(in11) in R
        z = int(in11) - 1
        if y == True and z >= 0:
                z1 = K[z]
                update_for_key_att_m(db_f,z1,sm)
        else:
                print('Введите корректный номер записи!')
