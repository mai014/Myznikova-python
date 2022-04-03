n = int(input('Введите кол-во человек: '))
tree = dict()
for i in range(n-1):
    print(i+1, 'пара:', end=' ')
    child, parent = input().split()
    tree[child] = parent
res = dict()
for parent in tree.values():
    if parent not in tree.keys():
        res[parent] = 0
for child in tree.keys():
    res[child] = res[tree[child]] + 1
print('"Высота" каждого члена семьи:')
for key in sorted(res):
    print(key, res[key])