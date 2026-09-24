
print('=' * 15, 'FitLife Console Bot', '=' * 15)
print('~' * 15, 'Добро пожаловать!!!', '~' * 15)

user_name = input('Как вас зовут?: ').capitalize()
user_age = int(input('Сколько вам лет?: '))
user_weight = float(input('Какой у вас вес? (в кг): '))
user_height = float(input('Какой у вас рост? (в метрах): '))

bmi = user_weight / (user_height ** 2)
water_ml = user_weight * 30
water_l = water_ml / 1000

print('-' * 22, 'Итоги', '-' * 22)
print(f'Вас зовут {user_name}, вам {user_age} лет!')
print(f'Ваш ИМТ: {round(bmi, 1)}.')
print(f'Рекомендуемая норма воды: {round(water_l, 3)} литров.')
print('Расчет окончен. Будьте здоровы!')
