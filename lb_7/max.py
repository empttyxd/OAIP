def max(num):
    if len(num) == 1:
        return num[0]

    a = max(num[1:])
    return num[0] if num[0] > a else a