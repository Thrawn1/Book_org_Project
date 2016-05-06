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
                S3 = key_book_sort(K)
                if t == 1:
                        return S1
                elif t == 2:
                        return S2
                elif t == 3:
                        return S3
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
                S3 = key_book_sort(K)
                if t == 1:
                        return S1,K1
                elif t == 2:
                        return S2,K2
                elif t == 3:
                        return S3
        else:
                print('Ошибка передачи аргумента в функцию archive_short!')