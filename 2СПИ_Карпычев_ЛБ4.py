def main():
    # 1 задание

    a = ""

    for _ in range(1, 9):
        b = input("Введите число: ")
        a += b
    print(a)

    # 2 задание

    n = int(input("Введите количество имен: "))
    names = []

    for _ in range(n):
        name = input("Введите имя: ")
        names.append(name)

    for i in range(n):
        print(f"{i + 1}. {names[i]}")

    # 3 задание

    for i in range(
            int(input("Введите дату с которой начать поиск: ")),
            32,
            int(input("Введите шаг: ")),
    ):
        print(i, end=" ")

    # 4 задание

    letter = input("Введите букву: ")
    n = int(input("Введите количество вводимых букв: "))
    letters = []
    count = 0
    max_count = 0
    print("Введите буквы: ")

    for i in range(n):
        letters.append(input())
        if letters[i] == letter:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count)

    # 5 задание

    x = int(input("Введите число: "))
    s = 0

    for i in range(1, x):
        if x % i == 0:
            s += i
    print(s + x)

    # 6 задание

    glas = ["а", "я", "о", "ё", "э", "е", "у", "ю", "ы", "и"]
    x = input("Введите строку: ").lower().split(" ")
    print(x)
    count_bez = 0

    for i in x:
        count_glas = 0
        for j in i:
            if j in glass:
                count_glas += 1
        if count_glas > 1:
            count_bez += count_glas - 1
    print("Всего безударных", count_bez)

    # 7 задание

    word = input("Введите слово: ")
    n = int(input("Ведите натуральное число: "))

    for i in range(n):
        print(word)

    # 8 задание

    num = input("Введите номер телефона: ")
    a = "+0123456789"

    if num[0] != "+" and num[0] != "8":
        print("Неправильный номер телефона!")

    elif num[0] == "+" and num[1] != "7":
        print("Неправильный номер телефона!")

    for i in num:
        if i not in a:
            print("Неправильный номер телефона!")
            break

    # 9 задание

    password = input("Введите пароль из русских букв: ").lower()
    glas = "ёуеыаоэяию"
    sogl = "цкнгшщзхфвпрлджчсмтбъьй"
    result = ""

    for i in password:
        if i in glas:
            result += "0"
        elif i in sogl:
            result += "1"
    print(result)

    # 10 задание

    message = "ППррииввеетт!!  ККаакк  ддееллаа??  ССееггоодднняя  ттааккааяя  ххоорроошшааяя  ппооггооддаа,,  ммоожжеетт  ппооггуулляяеемм??"
    for i in range(0, len(message), 2):
        print(message[i], end="")


if __name__ == "__main__":
    main()
