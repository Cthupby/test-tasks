'''
Задача
Разработать программу для вычисления кратчайшего пути для почтальона.
Описание задачи
Почтальон выходит из почтового отделения, объезжает всех адресатов один раз для вручения посылки и возвращается в почтовое отделение.
Необходимо найти кратчайший маршрут для почтальона.
Координаты точек
    Почтовое отделение – (0, 2)
    Ул. Грибоедова, 104/25 – (2, 5)
    Ул. Бейкер стрит, 221б – (5, 2)
    Ул. Большая Садовая, 302-бис – (6, 6)
    Вечнозелёная Аллея, 742 – (8, 3)
'''

points = [
    (0, 2), 
    (2, 5), 
    (5, 2), 
    (6, 6), 
    (8, 3)
    ]

i = 0
start = points[i]


def a_distance(point: int, points: list, lap):

    init_c = points[point]
    
    if len(points) == 1:
        points.append(start)
        laps = ((init_c[0] - points[1][0]) ** 2 + (init_c[1] - points[1][1]) ** 2) ** 0.5
        lap += laps
        return lap
        
    all_laps = []
    
    for i, c in enumerate(points):
        laps = ((init_c[0] - c[0]) ** 2 + (init_c[1] - c[1]) ** 2) ** 0.5
        all_laps.append(laps)
    return m_distance(all_laps, points, point, lap)


def m_distance(l_distances: list, points: list, point: int, lap):

    points.pop(point)
    l_distances.remove(0.0)
    point = l_distances.index(min(l_distances))
    
    if l_distances:
        lap += min(l_distances)
        print(points[point])
        print(lap)

    return a_distance(point, points, lap)


if __name__ == '__main__':
    print(a_distance(i, points, i))