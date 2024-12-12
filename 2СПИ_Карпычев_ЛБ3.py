def main():
    
    while True:
        x = input()
        if x == "":
            break
    print(len(x))

# 2 задание

    count = 0
    while True:
        x = float(input())
        if x > 36.6:
            break
        elif x <= 36.6:
            count += 1
    print(count)

# 3 задание

    m_num = [-999]
    while True:
        num = float(input())
        if num >= 1000 or num <= -1000:
            break
        if num > m_num[-1]:
            m_num += [num]
    print(m_num[-2])


# 4 задание

    num = input()
    num_list = num.split(" ")
    num_list = list(map(float, num_list))
    min_num = num_list[0]
    counter = 1
    while counter < len(num_list):
        if num_list[counter] < min_num:
            min_num = num_list[counter]
            counter += 1
    print(min_num)

# 5 задание

    num = float(input())
    while True:
        if num == 0:
            break
        elif num % 3 == 0 and num % 7 == 0:
            print("Караул!")
            break
        elif num % 3 == 0 and num % 7 != 0:
            print("Несчастливое")
        elif num % 7 == 0 and num % 3 != 0:
            print("Опасное")
        else:
            print(num)
            num = float(input())

# 6 задание

    a = 0
    num = 1
    while num <= 10000:
        if num % num == 0 and num % 1 == 0:
            a += num
            num += 1
        else:
            break
        print(a)

# 7 задание

# 8 задание

    word = [input()]
    small_word = [word[0]]
    while word[-1] != "стоп":
        if len(word[-1]) < len(small_word[-1]):
            small_word = [word[-1]]
        word.append(input())
        print(small_word[0])

# 9 задание

    num = float(input())
    operator = input()
    result = num
    while operator != "стоп":
        num = float(input())
        if operator == "+":
            result += num
        elif operator == "-":
            result -= num
        elif operator == "*":
            result *= num
        elif operator == "/":
            result /= num
        elif operator == "**":
            result **= num
    print(result)
    operator = input()

# 10 задание

    result = ""
    while True:
        word = input()
        if word == "стоп":
            break
        result += word + " "
        if word == "!":
            result = result[:-3] + "!"
        result += "\n"
        print(result)


if __name__ == "__main__":
    main()
