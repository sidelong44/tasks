print('Введите целое число A:')
a = int(input())
print('Введите целое число B:')
b = int(input())
if (a > b):
    raise TypeError('A должно быть меньше или равно B')

result = ''
for i in range(a, b + 1):
    if (i % 2 == 0):
        if (len(result)):
            result += ' '
        result += str(i)

print(result)