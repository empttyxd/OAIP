def main():

    #Задание 1

    movie, cinema, time = input(), input(), input()
    print(f'Билет на " {movie} " в " {cinema} " на " {time} " забронирован.')

    # Задание 2

    money = int(input('Зарплата за месяц:\n>>>'))
    hours = int(input('Количество отработанных в выходные часов:\n>>>'))
    print(f'Размер премии: {money * 0.01 * hours}')

    # Задание 3

    sum = int(input('Введите сумму:\n>>>'))
    print(f'{sum % 10} - по 1р')
    print(f'{sum % 100 // 10} - по 10р')
    print(f'{sum % 1000 // 100} - по 100р')
    print(f'{sum // 1000} - по 1000р')

    # Задание 4

    text = input('Оцените развлекательный комплекс:\n>>>')
    print(text.find("весело"))
    print(text.find("увлекательно"))
    print(text.find("развлечения"))

    # Задание 5

    a = input()
    print(a[(len(a) - 1) // 2])

    # Задание 6

    feedback = "Алиса и Вася, большое спасибо за теплый приём!"
    name1 = feedback[0:5]
    name2 = feedback[8:12]
    print(f'Назначить премию: {name1}/{name2}')

    # Задание 7

    a = int(input())
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if a + 3 > len(alphabet):
        alphabet = alphabet * 2
        print(alphabet[a - 1:a + 3])
    else:
        print(alphabet[a - 1:a + 3])

    # Задание 8

    my_list = []
    my_list = [1, 2, 3, 4, 5]

    my_list.append(6)
    my_list.extend([7, 8])
    print(my_list)

    my_list.remove(3)
    print(my_list)
    pop_list = my_list.pop(0)
    print(my_list)
    print(pop_list)

    slice_list = my_list[1:4]
    print(slice_list)

    # метод reverse
    my_list.reverse()
    print(my_list)

    # через срез
    reversed_list = my_list[::-1]
    print(reversed_list)

    two_dimensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(two_dimensional_list)

    element = two_dimensional_list[1][2]
    print(element)

    two_dimensional_list[0][0] = 10
    print(two_dimensional_list)

    my_list.clear()
    print(my_list)

    # Задание 9

    empty_tuple = ()
    print(empty_tuple)

    filled_tuple = (1, 2, 3, 5.5)
    print(filled_tuple)

    # Задание 10

    empty_set = set()
    print(empty_set)

    my_set = {1, 2, 3, 4}
    print(my_set)

    empty_set.add(5)
    empty_set.add(10)
    print(empty_set)

    # Задание 11

    empty_dict = {}
    print(empty_dict)

    my_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
        }
    print("Словарь с элементами:", my_dict)

    my_dict["job"] = "Engineer"
    print("После добавления значения 'job':", my_dict)

    removed_value = my_dict.pop("age")
    print("После удаления значения 'age':", my_dict)
    print("Удаленное значение:", removed_value)

    my_dict["city"] = "San Francisco"
    print("После изменения значения 'city':", my_dict)


if __name__ == "__main__":
    main()




