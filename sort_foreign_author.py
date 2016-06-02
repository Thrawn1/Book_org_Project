import shelve
from key_book_sort import *
def sort_foreign_author(j,K):
        T = []
        T1 = []
        for key in K:
                z = key.foreign_author
                if z == False:
                        T.append(key)
                elif z == True:
                        T1.append(key)
                else:
                        print('Ошибка определения автора!')
        D = key_book_sort(T)
        F = key_book_sort(T1)
        if j == 1:
                return D
        elif j == 2:
                return F
        