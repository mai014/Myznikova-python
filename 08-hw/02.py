members = 0
for i in range(1, 11):
    print('Введите', i, 'возглас: ', end='')
    ans = input()
    if ans == 'Карамба':
        members += 1
print(members, 'человек теперь в команде!')