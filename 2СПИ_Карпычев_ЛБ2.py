def main():

    # Задание 1

    a = input()

    if a == "Python":
        print("ДА")
    else:
        print("НЕТ")

    # Задание 2

    a, b = input(), input()

    if a == "да" and b == "да":
        print("ВЕРНО")
    elif a == "нет" and b == "нет":
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")

    # Задание 3

    a, b, c = input(), input(), input()

    if a == "раз" and b == "два" and c == "три" or a == "1" and b == "2" and c == "3":
        print("ГОРИ")
    else:
        print("НЕ ГОРИ")

    # Задание 4

    july_city, august_city = input(), input()

    if (july_city == "Тула" and august_city != "Пенза" and july_city != august_city) or (july_city != "Тула" and august_city == "Пенза" and july_city != august_city):
        print("ДА")
    else:
        print("НЕТ")

    # Задание 5

    import math

    n, m = float(input()), float(input())

    if m <= 0 or n <= 0:
        print("Количество километров за день должно быть положительным числом.")
    else:
        days = math.ceil(n / m)
        print(f'Спортсмен добежит до финиша на {days} день.')

    # Задание 6

    num = int(input())
    num1 = num // 100
    num2 = num // 10 % 10
    num3 = num % 10
    sum = num1 + num3

    if sum % 8 == 0 and num2 != 3:
        print(f'НЕПОДХОДИТ {sum} {num2}')
    else:
        print(f'ПОДХОДИТ {sum} {num2}')

    # Задание 7

    product = input("Введите категорию товара:")

    if product == "продукты":
        price = int(input("Введите цену:"))
        if price < 100:
            print("Попробуйте нашу выпечку!")
        elif 100 >= price < 500:
            print("Как насчёт орехов в шоколаде?")
        elif 500 <= price:
            print("Попробуйте экзотические фрукты!")
    else:
        print("Загляните в товары для дома!")

    # Задание 8

    price1 = int(input("Цена первого товара:"))
    price2 = int(input("Цена второго товара:"))
    price3 = int(input("Цена третьего товара:"))
    sum = price1 + price2 + price3

    if price1 < price2 < price3:
        print("Акция!")
        print("К оплате:", sum / 2)
    elif price1 > price2 > price3:
        print("Акция!")
        print("К оплате:", sum / 3)
    else:
        print("К оплате:", sum)

    # Задание 9

    before_yesterday = int(input("Введите число покупателей за позавчера:"))
    yesterday = int(input("Введите число покупателей за вчера:"))
    if before_yesterday < yesterday:
        print(f'Сегодня магазин посетит {yesterday + (yesterday - before_yesterday)} человек')
    if yesterday < before_yesterday:
        print(f'Сегодня магазин посетит {yesterday - (before_yesterday - yesterday)} человек')
    if yesterday == before_yesterday:
        print(f'Сегодня магазин посетит {yesterday} человек')

    # Задание 10

    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Год високосный")
    else:
        print("Год не является високосным")

    # Задание 11

    x = int(input())

    if x % 2 == 0:
        print("Число является четным")
    else:
        print("Число является нечетным")


if __name__ == "__main__":
    main()
