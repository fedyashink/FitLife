print("=" * 15, "FitLife Console Bot", "=" * 15)
print("~" * 15, "Добро пожаловать!!!", "~" * 15)

while True:
    try:
        user_name = input("Как вас зовут?: ").capitalize()

        if not user_name.isalpha():
            raise ValueError

        break
    except ValueError:
        print("Имя должно содержать только буквы. Попробуйте снова.")

while True:
    try:
        user_age = int(input("Сколько вам лет?: "))

        if user_age <= 0:
            raise ValueError

        break
    except ValueError:
        print("Вы ввели возраст неверно. Попробуйте снова.")

while True:
    try:
        user_weight = float(input("Какой у вас вес? (в кг): "))

        if user_weight <= 0:
            raise ValueError

        break
    except ValueError:
        print("Вы ввели вес неверно. Попробуйте снова.")

while True:
    try:
        user_height = float(input("Какой у вас рост? (в метрах): "))

        if user_height <= 0 or user_height > 2.72:
            raise ValueError

        break
    except ValueError:
        print("Вы ввели рост неверно. Попробуйте снова.")

bmi = user_weight / (user_height ** 2)
water_ml = user_weight * 30
water_l = water_ml / 1000

print("-" * 5, f"Результаты пользователя {user_name}({user_age} лет)", "-" * 5)

print(f"Ваш ИМТ: {round(bmi, 1)}, ", end="")

if bmi < 18.5:
    print("у вас недостаток веса.")

elif 18.5 <= bmi <= 24.9:
    print("у вас здоровый вес.")

elif 25 <= bmi <= 29.9:
    print("у вас избыточный вес.")

else:
    print("у вас ожирение.")

print(f"Рекомендуемая норма воды: {round(water_l, 3)} литров.")
print("Расчет окончен. Будьте здоровы!")
