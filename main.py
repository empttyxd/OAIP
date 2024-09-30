# string = input()
# if string == "Python":
#     print('yes')
# else:
#     print('no')

# word1, word2 = input(), input()
# if word1 == 'да' and word2 == 'да':
#     print('ВЕРНО')
# elif word1 == 'нет' and word2 == 'нет':
#     print('ВЕРНО')
# else:
#     print('НЕВЕРНО')
#
# a = input()
# b = input()
# c = input()
# if a == 'раз' and b == 'два' and c == 'три':
#     print('ГОРИ')
# elif '1' in a and '2' in b and '3' in c:
#     print('ГОРИ')
# else:
#     print('НЕ ГОРИ')

# city_july = input()
# city_august = input()
# if city_july == 'Тула' or city_august == 'Пенза':
#     print('ДА')
# else:
#     print('НЕТ')

# n, m = int(input()), int(input())
# if n and m != 0:
#     x = n // m
#     print(x)
# else:
#     print('Ошибка')

# num = int(input())
# if ((num // 100 % 100) + (num % 10)) % 8 != 0 and num // 10 % 10 == 3:
#     print("ПОдходит")
# else:
#     print(num // 100 % 100 + num % 10, num // 10 % 10)

a,b = input("Категория:"),0
if a == "Продукты":
    print('Введите цену:')
    b == int(input())
    if b < 100:
        print("Попробуйте нашу выпечку!")
    if b >= 100 and b < 500:
        print("Как насчет орехов в шоколаде?")
    elif b >= 500:
        print('Попробуйте экзотические фрукты!')
    else:
        print("Загляните в товары для дома!")








