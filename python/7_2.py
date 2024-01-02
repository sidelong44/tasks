print('Введите строку:')
value = input()
if (len(value) > 1000):
    raise TypeError('Длина строки не должна превышать 1000 символов')

while '  ' in value:
    value = value.replace('  ', ' ')
print(value)