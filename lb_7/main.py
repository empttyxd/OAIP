from factorial import factorial
from fibonacci import fibonacci
from letters import letters
from simple import simple
from main import max

def main():
    print(factorial(5))
    print(fibonacci(5))
    print(letters("Как у тебя дела?"))
    print(simple(5))
    print(max(num = [3, 5, 2, 8, 1]))


if __name__ == '__main__':
    main()