print('Введите натуральное число:')
value = int(input())
if value < 1:
    raise TypeError(str(value) + ' не является натуральным числом')
elif value > 2*10**9:
    raise TypeError('Ограничение задачи')

delimiter = 2
degree = 0
count = 1
while value >= 1:
    if (value % delimiter == 0):
        degree += 1
        value = value // delimiter
    else:
        count *= (degree + 1)
        degree = 0
        delimiter += 1
        if value == 1:
            break
print('Количество натуральных делителей:', count)