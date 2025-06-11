def letters(s):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    if not s:
        return 0
    else:
        return (s[0] in vowels) + letters(s[1:])
