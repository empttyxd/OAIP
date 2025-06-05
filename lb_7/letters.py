def letters(s):
    glasnye = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'

    if not s:
        return 0

    first_glasnye = s[0] in glasnye

    return (1 if first_glasnye else 0) + count_glasnye(s[1:])