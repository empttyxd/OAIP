def main():
    # 1 задание

    a = int(input("Введите количество номеров: "))
    dig = set()

    for i in range(a):
        dig |= set(input("Введите номер: "))
    print(len(dig))

    # 2 задание

    word1 = set(input("Введите 1 слово: "))
    word2 = set(input("Введите 2 слово: "))
    word3 = set(input("Введите 3 слово: "))
    print("".join(word1 & word2 | word1 & word3 | word2 & word3))

    # 3 задание

    dig = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    num = input("Введите число: ")
    num_set = set()
    for i in num:
        num_set.add(i)
    print(" ".join(dig - num_set))

    # 4 задание

    num = []
    res = []
    while True:
        num = int(input("Введите число: "))
        if num == 0:
            break
        num.append(num)
    for i in num:
        if i % len(num) == 0:
            res.append(i)
    print(res)

    # 5 задание

    num_colors = int(input("количество цветов: "))
    colors = []
    for i in range(num_colors):
        colors.append(input("Цвет: "))
    num_flags = int(input("количество флагов: "))
    res = []
    for i in range(num_flags):
        index = i % num_colors
        color = colors[index]
        res.append(color)
    print("\n".join(res))

    # 6 задание

    period = []
    while True:
        age = input("возраст находки: ")
        if age == "":
            break
        if int(age) * 1000 in range(635000000, 2800000000):
            period.append("Proterozoic")
        elif int(age) * 1000 in range(300000000, 635000000):
            period.append("Paleozoic")
        elif int(age) * 1000 in range(145000000, 300000000):
            period.append("Mesozoic")
        elif int(age) * 1000 in range(145000000):
            period.append("Cenozoic")
        else:
            period.append("Archaea")
    print('\n'.join(period))


if __name__ == "__main__":
    main()