from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    price: int


def sorting(book):
    return sorted(book, key=lambda b: b.year)


book = [Book('Записки из подполья', 'Ф. М. Достоевский', 1866, 210),
        Book('Детство. Отрочество. Юность', 'Л. Н. Толстой', 1869, 300),
        Book('Анна Каренина', 'Л. Н. Толстой', 1877, 250),
        Book('Записки юного врача', 'М. А. Булгаков', 1967, 230),
        Book('Тихий Ден', 'Ozon761games', 1940, 280)]

sorted_book = sorting(book)
for i in sorted_book:
    print(i.title, i.author, i.year, i.price)
