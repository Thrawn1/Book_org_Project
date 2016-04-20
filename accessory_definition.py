import shelve
def accessory_file(db_f,z1):
        h = db_f[z1].accessory
        if h == False:
                h1 = 'Книга своя'
        else:
                h1 = 'Книга чужая'
        return h1
def accessory_class(tmp_book):
        h = tmp_book.accessory
        if h == False:
                h1 = 'Книга своя'
        else:
                h1 = 'Книга чужая'
        return h1