price = int(input('Введите стоимость квартиры (млн р): '))
square = int(input('Введите её площадь (м2): '))
if (price <= 10 and square >= 100) or (price <= 7 and  80 <= square < 100):
    print('Эта квартира вам подходит!')
else:
    print('Эта квартира вам не подходит!')