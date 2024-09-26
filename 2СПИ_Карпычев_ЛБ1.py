film = input()
cinema = input()
time = input()
print(f'Билет на " {film} " в " {cinema} " на {time} забронирован.')

salary = int(input('Зарплата за месяц:'))
x = int(input('Количество отработанных в выходных часов:'))
prise = salary * 0.01 * x
print('Размер премии:', prise)

sum = int(input('Введите сумму:'))
banknote_1000 = sum // 1000
sum1 = sum - (1000 * banknote_1000)
banknote_100 = sum1 // 100
sum2 = sum1 - (100 * banknote_100)
coin_10 = sum2 // 10
sum3 = sum2 - (10 * coin_10)
coin_1 = sum3 // 1
print(coin_1, '- по 1р')
print(coin_10, '- по 10р')
print(banknote_100, '- по 100р')
print(banknote_1000, '- по 1000р')

asd = input('Оцените развлекательный комплекс:')
print(asd.find('весело'))
print(asd.find('увлекательно'))
print(asd.find('развлечения'))

zxc = input()
print(zxc[(len(zxc)-1)//2])
gg = 'Алиса и Вася, большое спасибо за теплый приём!'
name1 = gg[0:5]
name2 = gg[8:12]
print("Назначить премию:", name1 + '/' + name2)

numb = int(input())
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if numb + 3 > len(symbols):
    alphabet = symbols * 2
    print(alphabet[numb - 1:numb + 3])
else:
    print(symbols[numb - 1:numb + 3])

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.insert(0, 0)
my_list.remove(3)
del my_list[0]
slice = my_list[1:4]
reversed_list = my_list[::-1]
my_list.reverse()
two_dimensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list.clear()
empty_tuple = ()
filled_tuple = (1, 2, 3, 4, 5)
print(empty_tuple)
print(filled_tuple)

empty_set = set()
my_set = {1, 2, 3, 4, 5}
empty_set.add(6)
empty_set.add(7)
union_set = my_set.union(empty_set)
intersection_set = my_set.intersection(empty_set)
difference_set = my_set.difference(empty_set)
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['email'] = 'john@example.com'
del my_dict['city']
my_dict['age'] = 31





