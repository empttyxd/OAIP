def brackets(s):

    smthg = {')': '(', ']': '[', '}': '{', '>': '<'}
    a = []

    for b in s:
        if b in smthg.values():
            a.append(b)
        elif b in smthg.keys():
            if not a or a.pop() != smthg[b]:
                return False

    return len(a) == 0