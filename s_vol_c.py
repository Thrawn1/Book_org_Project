from author_class import *
class S_vol(Author):
        #Данный класс описывает книгу, которая не имеет томов
        def __init__(self,name_book='',year_p = 0,genre ='',location = 0,accessory = False,voluminous = False,archive = False ,comment_archive = '',data_creating='',data_last_editing='',data_archive=''):
                #name - название книги
                #genre - жанар книги 
                # year_p - год издания книги;
                #accessory - чужая ли книга(True - чужая,False - своя);
                #location - полка, на которой находится книга
                #voluminous - признак многотомности книги
                self.name_book = name_book
                self.year_p = year_p
                self.accessory = accessory
                self.genre = genre
                self.location = location
                self.voluminous = voluminous
                self.archive = archive
                self.comment_archive = comment_archive
                self.data_creating = data_creating
                self.data_last_editing = data_last_editing
                self.data_archive = data_archive
        def author_family(self):
        # Данная функция позволит получать Фамилию автора
                return self.author.split()[0]
        def accessory_type(self):
                h = self.accessory
                if h == False:
                        h1 = 'Книга своя'
                else:
                        h1 = 'Книга чужая'
                return h1
        def voluminous_type(self):
                sm = self.voluminous
                if sm == False:
                        sm1 = 'Книга имеет один том'
                elif sm == True:
                        sm1 = 'Книга имеет несколько томов'                       
                else:
                        print('Ошибка определения атрибута многотомности')
                        sm1 = ''
                return sm1
        def archive_type(self):
                j = self.archive
                if j == True:
                        jj = 'Книга в архиве'
                elif j == False:
                        jj = 'Книга не в архиве'
                else:
                        print('Ошибка определения атрибута архива')
                        jj = ''
                return jj