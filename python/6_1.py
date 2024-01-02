print('Введите количество чисел:')
count = int(input())
nullable_count = 0
for i in range(count):
    print('Введите целое число:')
    value = int(input())
    if value == 0:
        nullable_count += 1
print('Количество равных нулю:', nullable_count)
