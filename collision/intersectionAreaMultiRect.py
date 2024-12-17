class RectCorrectError(Exception):
    pass



def intersectionAreaMultiRect(rectangle):
    if not rectangle:
        return 0  # Если список пустой, пересечение = 0

    for rect in rectangle:
        (x1, y1), (x2, y2) = rect
        if x1 >= x2 or y1 >= y2:
            raise RectCorrectError(f"Некорректный прямоугольник: {rect}")

    intersection = rectangle[0]  # Начинаем с первого прямоугольника

    # Поочередно пересекаем с каждым прямоугольником из списка
    for rect in rectangle[1:]:
        (x1, y1), (x2, y2) = intersection
        (x3, y3), (x4, y4) = rect

        left = max(x1, x3)#левая граница пересечения
        lower = max(y1, y3)#нижняя граница
        right = min(x2, x4)#правая граница
        upper = min(y2, y4)#верхняя граница

        if left < right and lower < upper:
            width=right-left
            height=upper-lower
        else:
            return 0  # Если нет пересечения, возвращаем 0
    # Вычисляем площадь
    
    return (width) * (height)


# Пример использования
rectangles_list = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)],
]

result = intersectionAreaMultiRect(rectangles_list)
print(f"Уникальная площадь пересечения: {result}")