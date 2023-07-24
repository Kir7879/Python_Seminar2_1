print('Количество чисел n')
n = int(input('n:='))
print('Монетка лежит гербом вверх - 1')
print('Монетка лежит решкой вверх - 0')
print('Ввести только 0 или 1')
count = 0
count_0 = 0
for i in range(n):
    x = int(input())
    i += 1
    if x == 1:
        count += 1
    if x == 0:
        count_0 += 1
if count < count_0:
    print('Минимальное количество операции', count)
else: 
    print('Минимальное количество операции', count_0)


