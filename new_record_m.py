from protect_fields import *
def multi_book(self):
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
                    setattr(self,field,new_b)
                    rt = rt+1
                else: pass
        elif field == 'number_vol':
            while cb != 1:
                new_b = input('\t[%s]\nВведите номер тома:' % (field_1))
                cb = protect_total_vol(new_b)
                if cb == 1:
                    setattr(self,field,new_b)
                    rt = rt+1
                else: pass
        elif field == 'availble_vol':
            while cb != 1:
                new_b = input('\t[%s]\nВведите  количество томов в наличии:' % (field_1))
                cb = protect_total_vol(new_b)
                if cb == 1:
                    setattr(self,field,new_b)
                    rt = rt+1
                else: pass
    return self
