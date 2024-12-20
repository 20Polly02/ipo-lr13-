from collision import *
# Проверяем корректность прямоугольника с помощью функции isCorrectRect
print("Функция isCorrectRect:")
print(isCorrectRect([(-3.4, 1), (9.2, 10)]))
print(isCorrectRect([(-7, 9), (3, 6)]))
# Проверяем пересечение двух прямоугольников с помощью функции isCollisionRect
print("Функция isCollisionRect:")
print(isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))
# Вычисляем площадь пересечения двух прямоугольников с помощью функции intersectionAreaRect
print("Функция intersectionAreaRect:")
print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
# Вычисляем уникальную площадь пересечения всех прямоугольников с помощью функции intersectionAreaMultiRect
print("Функция intersectionAreaMultiRect:")
result = intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")
incorrect_rectangles = [
    [(-3, 1), (9, 10)],
    [(3, 17), (13, 1)]
]
print(intersectionAreaMultiRect(incorrect_rectangles))