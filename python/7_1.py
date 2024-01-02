print('Введите строку без пробелов')
value = input()
if (' ' in value):
    raise TypeError('Требуется строка без пробелов')

result = print('yes' if value[::-1] == value else 'no')