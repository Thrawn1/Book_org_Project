from update_for_key_att_s import *
#from update_for_key_att_m import *
def update_for_key_att(db_f,R,K):
        in11 = input('Введите ключ записи, которую хотите отредактировать: ')
        y = int(in11) in R
        z = int(in11) - 1
        if y == True and z >= 0:
                z1 = K[z]
                sm = db_f[z1].voluminous
                if sm == False:
                        update_for_key_att_s(db_f,z1,sm)
#                elif sm == True:
#                        update_for_key_att_m(db_f,z1,sm)
                else:
                        print('Ошибка определения атрибута многотомности')
                
        else:
                print('Введите корректный номер записи!')
