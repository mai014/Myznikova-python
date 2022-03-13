N = int(input('Кол-во человек: '))
people = []
for i in range(1, N + 1):
    people.append(i)
count = int(input('Какое число в считалке? '))
print('Текущий круг людей:', people)
num_first = 0
while len(people) != 1:
    num_lost = num_first
    for _ in range(1, count):
        if num_lost == len(people) - 1:
            num_lost = 0
        else:
            num_lost += 1
    print('Выбывает человек под номером:', people[num_lost])
    people.pop(num_lost)
    if num_lost == len(people):
        num_first = 0
    else:
        num_first = num_lost
    print('Текущий круг людей:', people)
