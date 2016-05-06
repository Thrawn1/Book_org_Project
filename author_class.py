class Author:
        def __init__(self,author_name, author_middle_name, author_family, foreign_author = False):
                self.author_name = author_name
                self.author_middle_name = author_middle_name
                self.author_family = author_family
                self.foreign_author = foreign_author
        def author_name_and_family(self):
                c1 = str(self.author_name) + ' ' + str(self.author_family)
                c2 = str(self.author_family) + ' ' +str(self.author_name)
                c3 = c1.lower()
                c4 = c2.lower()
                return c3,c4
        def author_initial(self):
                j = []
                j.append(str(self.author_name))
                j.append(str(self.author_middle_name))
                m1 = j[0][0] + '.' + j[1][0] + '. ' + str(self.author_family)
                m2 = str(self.author_family) + ' '+ j[0][0] + '.' + j[1][0] +'.'
                m3 = j[0][0] +'.' + str(self.author_family) + j[1][0] + '.'
                m11 = m1.lower()
                m22 = m2.lower()
                return m11,m22
        def author_name_middle_q(self):
        #Данная функция позволяет получить имя и отчество автора
                i1 = str(self.author_name) +' '+ str(self.author_middle_name)
                i = i1.lower()
                return i
                
