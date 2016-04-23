import shelve
from print_results import *
def delete_from_db (db_f,z):
        print_results_search(z,db_f)
        u = input('Введите ключ: ')
        del db_f[u]
        
