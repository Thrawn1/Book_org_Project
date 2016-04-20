import shelve
def voluminous_book(db_f,z1):
        sm = db_f[z1].voluminous
        if sm == False:
                sm1 = 'Книга имеет несколько томов'
        elif sm == True:
                sm1 = 'Книга имеет несколько томов'
        else:
                print('Ошибка определения атрибута многотомности')