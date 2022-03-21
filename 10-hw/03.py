import random
team1 = [round(random.uniform(5.0, 10.0), 2) for _ in range(0, 20)]
team2 = [round(random.uniform(5.0, 10.0), 2) for _ in range(0, 20)]
result = [team1[i] if team1[i] > team2[i] else team2[i] for i in range(0, 20)]
print('Первая команда:', team1)
print('Вторая команда:', team2)
print('Победители тура:', result)
