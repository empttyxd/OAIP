def factorial(n):
    if n < 0:
        return 'error'
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print('factorial', 5, 'is', factorial(5))
