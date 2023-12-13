print('Введите сумму инвестиций:')
sum = float(input())
print('Введите количество денег Майкла:')
mike = float(input())
print('Введите количество денег Ивана:')
ivan = float(input())

mike_has_sum = sum <= mike
ivan_has_sum = sum <= ivan

if (mike_has_sum and ivan_has_sum):
    print(2)
elif (mike_has_sum):
    print('Mike')
elif (ivan_has_sum):
    print('Ivan')
elif (sum <= mike + ivan):
    print(1)
else:
    print(0)
