import shelve
def voluminous_book(db_f,z1):
        sm = db_f[z1].voluminous
        if sm == False:
                sm1 = 'Книга имеет один том'
                return sm1
        elif sm == True:
                sm1 = 'Книга имеет несколько томов'
                return sm1
        else:
                print('Ошибка определения атрибута многотомности')