
def definition_author():
        cv = 0
        print('\n\n\tВыберете, среди отечественных или зарубежных авторов проводить поиск')
        while cv != 1:
                in_1 = input('\n\n\t1 - Отечественный автор; 2 - Зарубежный автор: ')
                if in_1 == '1':
                        out_1 = 1
                        cv = 1
                        return out_1
                elif in_1 == '2':
                        out_1 = 2
                        cv =1
                        return out_1
                else:
                        print('\n\n\n\t\t\tОшибка! Выберете правильный пункт!')
                        cv = 0