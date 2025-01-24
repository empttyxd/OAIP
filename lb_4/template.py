import math


def template(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print(None)
        return

    perimeter = a + b + c
    s = perimeter / 2
    plochad = math.sqrt(s * (s - a) * (s - b) * (s - c))

    rvnb = ((a == b and b == c and a != c) or (b == c and a == c and a != b) or (a == b and a == c and b != c))
    rvns = (a == b == c)

    print(f"Периметр: {perimeter}")
    print(f"Площадь: {plochad}")
    if rvnb:
        print("Равнобедренный: да")
    else:
        print("Равнобедренный: нет")
    if rvns:
        print("Равносторонний: да")
    else:
        print("Равносторонний: нет")
