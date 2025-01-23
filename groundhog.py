def groundhog_day(data1):
    if len(data1) < 2:
        return (0, 0)

    for i in range(1, len(data1)):
        current_str = data1[i]
        old_str = data1[i - 1]

        sym_diff = []
        for y in range(len(current_str)):
            if current_str[y] != old_str[y]:
                sym_diff.append(y)

        if len(sym_diff) > 2:
            return (i, *sym_diff)

    return (0, 0)