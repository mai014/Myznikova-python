N = 30
violation = 0
while N <= 35:
    print('Людей в', N, '-м секторе: ', end="")
    people = int(input())
    if people <= 10:
        print('Всё спокойно.')
    else:
        print('Нарушение! Слишком много людей в секторе!')
        violation += 1
    N += 1
print('Количество нарушений:', violation)