goods = {'Лампа': '12345', 'Стол': '23456', 'Диван': '34567', 'Стул': '45678'}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ]
}
num = 0
sum_price = 0
for name_good, pin_good in goods.items():
    for key_store, pin_store in store.items():
        if pin_good == key_store:
            for elem in pin_store:
                num += elem['quantity']
                sum_price += elem['quantity'] * elem['price']
    print(name_good, '-', num, 'штук, стоимость', sum, 'руб.')
    num = 0
    sum_price = 0
