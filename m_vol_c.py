#! /usr/bin/env python
# -*- coding: utf-8 -*-
from s_vol_c import *
class M_vol(S_vol):
        #Данный класс описывает книгу, которая имеет несколько томов. Наследуется от класса книги без томов
	def __init__(self,author,name,year_p,total_vol,number_vol,availble_vol,genre='',location=0,accessory = False):
                #total_vol - всего томов в собрании;
                #availble_vol - всего томов имеется в библиотеке;
                #availble_vol - текущий номер тома
                super().__init__(author,name,year_p,genre,location,accessory)
                self.total_vol = total_vol
                self.number_vol = number_vol
                self.availble_vol = availble_vol
