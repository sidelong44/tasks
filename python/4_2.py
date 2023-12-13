print('Введите пятизначное число:')
value = int(input())
if value > 99999 or value < 10000:
    raise ValueError('Некорректное значение. Ожидается целое пятизначное число')

units_count = value % 10
tens_count = value // 10 % 10
hundreds_count = value // 100 % 10
thousands_count = value // 1000 % 10
ten_thousands_count = value // 10000 % 10

result = tens_count ** units_count * hundreds_count / (ten_thousands_count - thousands_count)

print('Результат:', result)
