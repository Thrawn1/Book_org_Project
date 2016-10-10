from key_book_sort import *
def archive_short(v,t,db_f,K=[]):
        if v == 0:
                I1 = []
                I2 = []
                for key in K:
                        uu = db_f[key].archive
                        if uu == False:
                                I1.append(key)
                        elif uu == True:
                                I2.append(key)
                        else:
                                pass
                S1 = key_book_sort(I1)
                S2 = key_book_sort(I2)
                S3 = key_book_sort(K)
                if t == 1:
                        return S1
                elif t == 2:
                        return S2
                elif t == 3:
                        return S3
                else:
                        print ('Error! function [archive_short]')
        elif v == 1:
                I1 = []
                I2 = []
                for key in db_f:
                        uu = db_f[key].archive
                        if uu == False:
                                I1.append(key)
                        elif uu == True:
                                I2.append(key)
                        else:
                                pass
                S1 = key_book_sort(I1)
                S2 = key_book_sort(I2)
                if t == 1:
                        return S1
                elif t == 2:
                        return S2
                else:
                        print ('Error! function [archive_short]')
        elif v == 2:
                I1 = []
                I2 = []
                K1 = []
                K2 = []
                tmp_1 = 1
                tmp_2 = 1
                for key in db_f:
                        uu = db_f[key].archive
                        if uu == False:
                                I1.append(key)
                                K1.append(tmp_1)
                                tmp_1 = tmp_1 + 1
                        elif uu == True:
                                I2.append(key)
                                K2.append(tmp_2)
                                tmp_2 = tmp_2 + 1
                        else:
                                pass
                S1 = key_book_sort(I1)
                S2 = key_book_sort(I2)
                if t == 1:
                        return S1,K1
                elif t == 2:
                        return S2,K2
                else:
                        print ('Error! function [archive_short]')
        else:
                print('Ошибка передачи аргумента в функцию archive_short!')

#Параметрическая функция сортировки. Выполняет сортировку по заданному списку и по всему файлу. 
#Парамертр v - показывает, из чего будет производится сортировка - из заданного списка или из файла. По умолчанию передаваемый список пуст, а файл базы данных передается целиком. 1 - сортировка по списку, 2 - сортировка по файлу базы данных. 3 - сортировка по файлу базы данных(с нумерацией списков - созается параллельный список с номерами)
#Параметр t - показывает, что функция будет возвращать. 1 - возврат сортированного списка с признаком не архив. 2 - возврат сортированного списка с признаком архив. 3 - возврат сортированного списка ключей. 
