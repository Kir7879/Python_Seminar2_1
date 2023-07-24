print('Задумайте два целых числа Х и Y меньше или равно 1000')
print('Первая подсказка, сумма чисел X и Y равана S =')
S = int(input('S='))
print('Вторая подсказка, произведение чисел X и Y равана P =')
P = int(input('P='))
import math
d = S * S - 4 * P
print(d)
X1 = (S + round(math.sqrt(d), 2)) // 2
X2 = (S - round(math.sqrt(d), 2)) // 2
Y1 = S - X1
Y2 = S - X2
if X1 <= 1000 and Y1  <= 1000 or X2 <= 1000 and Y2 <= 1000:
    print(X1, Y1) 
    print(X2, Y2)
else:
    print('Загадай числа согласно требованиям')
