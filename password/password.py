from random import choice

alf = '+-#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

lenght = int(input('Введите длину пароля: '))
while lenght < 8:
    print('Пароль не подходит. Он кароче 8 символов')
    ans = input(f'Вы точно хотите пароль длинной {lenght}? да/нет')
    if ans == 'да':
        break
    lenght = int(input('Введите длину пароля'))


password = ''

for i in range(lenght):
    password += choice(alf)

print('Твой пароль -', password)
print(f'Твой пароль - {password}')
