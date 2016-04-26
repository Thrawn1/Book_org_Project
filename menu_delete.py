from delete_from_db import *
from delete_in_archive import *
def menu_delete(db_f):
        print('\n\n\tВыберете вариант удаления:\n\n1. Простое удаление в архив\n\n2.Полное удаление из базы(доступно по паролю для администратора системы)')
        in0 = input('\nВведите нужны пункт меню: ')
        if in0 == 1:
                delete_in_archive(db_f)
        elif in0 == 2:
                delete_from_db(db_f)
        else:
                print( '\n\nВведен не верный пункт меню или не допустимое значение!')
