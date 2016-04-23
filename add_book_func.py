import shelve
from new_record import *
def add_book_func(db_f):
#Данная функция была объявлена для удобства - теперь в menu.py все логично - формируется только меню и вызываются нужные функции, а не как раньше - добавление записи БД
# Возможно стоит переработать функцию new_record, и объединить с этой, что бы не усложнять проект
        j = new_record(db_f)
        K=[]
        print('Последние 15 записей:')
        for key in db_f:
                K.append(key)
                li = 0
                if li <15:
                        print('\t',db_f[key].author,db_f[key].name,db_f[key].year_p,('Полка №'+str(db_f[key].location)),'\n')
                else: pass
        print('Всего записей в базе данных:',len(K))
