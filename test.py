""" Тестовое задание
Создайте новый класс Hotel, который содержит поля название, стоимость, количество звездочек.
Экземпляры класса положите в список hotels.
– считать со стандартного ввода сумму
– подобрать 3 наиболее дорогих варианта размещения из тех, что подходят по стоимости
– вывести в формате "отель – количество звезд – стоимость"
– если таких вариантов меньше 3 – вывести сколько есть
– если таких вариантов нет – вывести "вариантов нет"
"""

class Hotel:
    def __init__(self, name, stars, price):
        self.name = name
        self.stars = stars
        self.price = price
    def __str__(self):
        return "{} {} {}".format(self.name, self.stars, self.price)

hotels = [
    Hotel('Atlantic Castle Hotel', 3, 45000),
    Hotel('Oriental Tide Hotel & Spa', 5, 92000),
    Hotel('Bronze Mansion Resort', 4, 84000),
    Hotel('Parallel Harbor Hotel', 4, 80000),
    Hotel('Obsidian Vertex Hotel', 5, 120000),
    Hotel('Noble Memorial Hotel', 4, 59000),
    Hotel('Mirth Hotel', 4, 64000),
    Hotel('Felicity Motel', 3, 29000),
    Hotel('Renaissance Hotel', 3, 49000),
    Hotel('Rainbow Hotel & Spa', 5, 154000),
]

enter = int(input())
i = 0
s_hotels = sorted(hotels, key=lambda hotel: hotel.price, reverse=True)

for hotel in s_hotels:
    while hotel.price <= enter and i < 3:
        print(hotel)
        i = i + 1
        break
if i == 0:
    print('вариантов нет')


