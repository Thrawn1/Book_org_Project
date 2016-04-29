from s_vol_c import *
class M_vol(S_vol):
        #Данный класс описывает книгу, которая имеет несколько томов. Наследуется от класса книги без томов
	def __init__(self,name_book='',year_p=0,total_vol=0,number_vol=0,availble_vol=0,genre='',location=0,accessory = False,voluminous = True,archive = False ,comment_archive = '',data_creating='',data_last_editing='',data_archive=''):
                #total_vol - всего томов в собрании;
                #availble_vol - всего томов имеется в библиотеке;
                #availble_vol - текущий номер тома
                super().__init__(name_book,year_p,genre,location,accessory,voluminous,archive,comment_archive,data_creating,data_last_editing,data_archive)
                self.total_vol = total_vol
                self.number_vol = number_vol
                self.availble_vol = availble_vol
