print('Введите целое число:')
value = int(input())

if (value == 0):
    print('нулевое число')
    exit()

is_odd = value % 2

result = 'положительное' if value > 0 else 'отрицательное'
result += ' '
result += 'нечетное' if is_odd else 'четное'
result += ' число'

print(result)

"""
Не знаю, зачем это дублировать, но в задании: "Если число не является четным - выведите сообщение "число не является четным""    
"""
if (is_odd):
    print('число не является четным')
