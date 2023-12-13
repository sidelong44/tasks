print('Введите слово из строчных латинских букв:')
value = input().lower()

vowels_map = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

for char in value:
    if (type(vowels_map.get(char)) == int):
        vowels_map[char] += 1
for vowel in vowels_map:
    count = vowels_map.get(vowel) or False
    print('"{vowel}": {count}'.format(vowel=vowel, count=count))
