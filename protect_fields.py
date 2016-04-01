def protect_name(in1):
    if in1 == '' or in1 == ' ' or in1 == '  ' or in1 == '   ':
        print('Введено не верное значение!')
        return 0
    else:
        return 1
def protect_author(in1):
    if in1 == '' or in1 == ' ' or in1 == '  ' or in1 == '   ':
        print('Введено не верное значение!')
        return 0
    else:
        return 1
def protect_date(in1):
    if in1.isdigit() == True:
        in2 = int(in1)
        if in2 > 1800 and in2 < 2500:
            return 1
        else:
             print('Введено не верное значение!')
             return 0
    else:
        print('Введите год!')
        return 0
def protect_location(in1):
    if in1.isdigit() == True:
        in2 = int(in1)
        if in2 > 0 and in2 < 10:
            return 1
        else:
             print('Введено не верное значение!')
             return 0
    else:
        print( 'Введите номер полки!')
        return 0
def protect_total_vol(in1):
    if in1.isdigit() == True:
        in2 = int(in1)
        if in2 > 0 and in2 < 100:
            return 1
        else:
             print('Введено не верное значение!')
             return 0
    else:
        print( 'Введите количество томов!')
        return 0
def protect_number_vol(in1):
    if in1.isdigit() == True:
        in2 = int(in1)
        if in2 > 0 and in2 < 100:
            return 1
        else:
             print('Введено не верное значение!')
             return 0
    else:
        print('Введите номер тома!')
        return 0
def protect_availble_vol(in1):
    if in1.isdigit() == True:
        in2 = int(in1)
        if in2 > 0 and in2 < 100:
            return 1
        else:
             print('Введено не верное значение!')
             return 0
    else:
        print('Введите количество томов в наличии!')
        return 0
def protect_number(in1):
    if in1.isdigit() == True:
        in2 = int(in1)
        if in2 > 0 and in2 < 100:
            return 1
        else:
             print('Введите корректное число строк,отображаемых на экране!')
             return 0
    else:
        print( 'Введите число!')
        return 0
