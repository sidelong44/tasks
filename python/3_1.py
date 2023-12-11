print('Введите вид животного:')
animal_type = input()
print('Введите возраст животного:')
animal_age = int(input())
print('Введите кличку животного:')
animal_name = input()

def get_age_title(age):
    if age in range(5, 20):
        return 'лет'
    last_dig = age % 10
    if 1 in (age, last_dig):
        return 'год'
    if last_dig in (2, 3, 4):
        return 'года'
    return 'лет'

print('Это ', animal_type, ' по кличке "', animal_name, '\". Возраст ', animal_age, ' ', get_age_title(animal_age), '.', sep='')