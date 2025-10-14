class MathUtils:
    pi = 3.14159
    e = 2.71828

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return 'error'
        return a / b

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def circle_area(radius):
        return MathUtils.pi * (radius ** 2)

    @staticmethod
    def is_even(number):
        return 'even' if number % 2 == 0 else 'odd'


print('sum:', MathUtils.add(1, 3))
print('Difference:', MathUtils.subtract(3, 1))
print('product of numbers:', MathUtils.multiply(2, 3))
print('Quotient of numbers:', MathUtils.divide(6, 3))
print('Raising to a power:', MathUtils.power(2, 3))
print('Area of ​​a circle:', MathUtils.circle_area(3))
print('Parity check:', MathUtils.is_even(4))
