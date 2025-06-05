def quarters(*data):
    count = {
        '1st': 0,
        '2nd': 0,
        '3rd': 0,
        '4th': 0
    }

    for i, j in data:
        if i > 0 and j > 0:
            count['1st'] += 1
        elif i < 0 and j > 0:
            count['2nd'] += 1
        elif i < 0 and j < 0:
            count['3rd'] += 1
        elif i > 0 and j < 0:
            count['4th'] += 1


    return count