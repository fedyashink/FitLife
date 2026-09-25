print("=" * 15, "FitLife Console Bot", "=" * 15)
print("~" * 15, "Добро пожаловать!!!", "~" * 15)

try:
    user_name = input("Как вас зовут?: ").capitalize()

    if not user_name.isalpha():
        raise ValueError

    user_age = int(input("Сколько вам лет?: "))
    user_weight = float(input("Какой у вас вес? (в кг): "))
    user_height = float(input("Какой у вас рост? (в метрах): "))

    if user_height > 2.5:
        raise ValueError

except ValueError:
    print("Кажется, вы ввели что-то неправильно...")
    print("Убедитесь в корректности данных и попробуйте снова.")

    user_name = input("Как вас зовут?: ").capitalize()
    user_age = int(input("Сколько вам лет?: "))
    user_weight = float(input("Какой у вас вес? (в кг): "))
    user_height = float(input("Какой у вас рост? (в метрах): "))

bmi = user_weight / (user_height ** 2)
water_ml = user_weight * 30
water_l = water_ml / 1000

print("-" * 22, "Итоги", "-" * 22)

print(f"Вас зовут {user_name}, вам {user_age} лет!")

print(f"Ваш ИМТ: {round(bmi, 1)}, ", end="")

if bmi < 18.5:
    print("у вас недостаток веса.")

elif 18.5 <= bmi <= 24.9:
    print("у вас нормальный, здоровый вес.")

elif 25 <= bmi <= 29.9:
    print("у вас избыточный вес.")

else:
    print("у вас ожирение.")

print(f"Рекомендуемая норма воды: {round(water_l, 3)} литров.")
print("Расчет окончен. Будьте здоровы!")
