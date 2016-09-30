from protect_fields import *
import datetime
def new_book(j,p=0):
        time = datetime.datetime.now()
        date_str = time.strftime("%d-%m-%Y")
        setattr(j,'data_creating',date_str)
        fieldnmes = ('foreign_author','author_family','author_name','author_middle_name','name_book','year_p','genre','location','accessory')
        fieldnmes_1 = ('Автор иностранный?','Фамилия автора','Имя автора','Отчество автора','Название книги','Год издания','Жанр','Где расположена книга','Чужая ли книга?')
        rt = 0
        for field in fieldnmes:
                cb = 0
                field_1 = fieldnmes_1[rt]
                if field == 'year_p':
                        while cb != 1:
                                new_b = input('\t[%s]\nВведите год издания:' % (field_1))
                                cb = protect_date(new_b)
                                if cb == 1:
                                        setattr(j,field,new_b)
                                        rt = rt+1
                                else: pass
                elif field == 'location':
                        while cb != 1:
                                new_b = input('\t[%s]\nВведите номер полки:' % (field_1))
                                cb = protect_location(new_b)
                                if cb == 1:
                                        setattr(j,field,new_b)
                                        rt = rt+1
                                else: pass
                elif field == 'accessory':
                        print('Пожалуйста выберете один из вариантов:\n1. Книга ваша\n2. Книга чужая')
                        new_b = int(input('\t[%s]\n:' % (field_1)))
                        if new_b == 1:
                                setattr(j,field,False)
                                rt = rt+1
                        elif new_b == 2:
                                setattr(j,field,True)
                                rt = rt+1
                        else:
                                print('Выбрано недопустимое значение!')
                elif field == 'genre':
                        new_b_1 = input('\t[%s]\nВведите жанр =>' % (field_1))
                        setattr(j,field,new_b_1)
                        rt = rt+1
                elif field == 'author_name':
                        while cb != 1:
                                new_b_1 = input('\t[%s]\nВведите имя автора:' % (field_1))
                                cb = protect_name_author(new_b_1)
                                if cb == 1:
                                        setattr(j,field,new_b_1)
                                        rt = rt+1
                                else: pass
                elif field == 'name_book':
                        while cb != 1:
                                new_b_1 = input('\t[%s]\nВведите название книги:' % (field_1))
                                cb = protect_name(new_b_1)
                                if cb == 1:
                                        setattr(j,field,new_b_1)
                                        rt = rt+1
                                else: pass
                elif field == 'author_family':
                        while cb != 1:
                                new_b_1 = input('\t[%s]\nВведите фамилию автора:' % (field_1))
                                cb = protect_family_author(new_b_1)
                                if cb == 1:
                                        setattr(j,field,new_b_1)
                                        rt = rt+1
                                else: pass
                elif field == 'author_middle_name':
                        while cb != 1:
                                new_b_1 = input('\t[%s]\nВведите отчество автора:' % (field_1))
                                cb = protect_middle_name_author(new_b_1)
                                if cb == 1:
                                        setattr(j,field,new_b_1)
                                        rt = rt+1
                                else: pass
                elif field == 'foreign_author':
                        print('Пожалуйста выберете один из вариантов:\n1. Автор отечественный\n2. Автор зарубежный')
                        new_b = int(input('\t[%s]\n:' % (field_1)))
                        if new_b == 1:
                                setattr(j,field,False)
                                rt = rt+1
                        elif new_b == 2:
                                setattr(j,field,True)
                                rt = rt+1
                        else:
                                print('Выбрано недопустимое значение!')
        if p == 0:
                return j
        elif p == 1:
                fieldnmes = ('total_vol','number_vol','availble_vol')
                fieldnmes_1 = ('Всего томов?','Номер тома','Всего томов есть в наличии')
                rt = 0
                for field in fieldnmes:
                        cb = 0
                        field_1 = fieldnmes_1[rt]
                        if field == 'total_vol':
                                while cb != 1:
                                        new_b = input('\t[%s]\nВведите общее количество томов в собрании:' % (field_1))
                                        cb = protect_total_vol(new_b)
                                        if cb == 1:
                                                setattr(j,field,new_b)
                                                rt = rt+1
                                        else: pass
                        elif field == 'number_vol':
                                while cb != 1:
                                        new_b = input('\t[%s]\nВведите номер тома:' % (field_1))
                                        cb = protect_total_vol(new_b)
                                        if cb == 1:
                                                setattr(j,field,new_b)
                                                rt = rt+1
                                        else: pass
                        elif field == 'availble_vol':
                                while cb != 1:
                                        new_b = input('\t[%s]\nВведите  количество томов в наличии:' % (field_1))
                                        cb = protect_total_vol(new_b)
                                        if cb == 1:
                                                setattr(j,field,new_b)
                                                rt = rt+1
                                        else: pass
                return j
        else:
                print('Ошибка создания новой записи о книге!')
#Данный модуль описывает функцию заполнения атрибутов класса. В данный модуль импортированы модуль проверки вводимых в разные атрибуты данных и модуль дата-время. 
#В переменной time вызывается метод класса time. В date_str получаем дату заданного формата. Далее вносим эту пременную как атрибут класса книга(многотомная или однотомная - неважно). 
#Далее идет описание атрибутов классов. Приведен список названий и их рускоязычный перевод. Это необходимо для того, что бы при вводе пользователю отображался русский текст и было понятно о каком параметре идет речь. Запускается поочередно цикд, в котром происходит опрос пользователя на ввод данных в поля атрибутов.
#Заполнение полей типовое, приведу пример на одном из полей. В цикле действует условие. Если поле в списке называется year_p, то выполеняется следующие условие: Запускается бесконечный цикл, пользователя просят ввести год издания книги. Когда пользоваль вводит символы, они заносятся в переменную new_b. Далее эта переменная передается в функцию protect_date() которая определяет, корректно ввели данные или нет. Функция возвращает 0 в случае неверных данных или 1 в случае верных. Если возвращается 1 то происходит запись атрибута и бесконечный цикл завершается. При нуле бесконечный цикл не заверщается, пользователя снова просят ввести правильный год издание книги.
#
#