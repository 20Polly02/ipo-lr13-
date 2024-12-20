from  .isCorrectRect import isCorrectRect
from .isCollisionRect import isCollisionRect

def intersectionAreaRect(rect_1,rect_2):
    if not isCorrectRect(rect_1):
        raise ValueError("Некорректный 1 прямоугольник.") 
    if not isCorrectRect(rect_2):
        raise ValueError("Некорректный 2 прямоугольник.")
    if isCollisionRect(rect_1,rect_2): # границы пересечения
        left = max(rect_1[0][0], rect_2[0][0])   # левая граница
        lower = max(rect_1[0][1], rect_2[0][1])  # нижняя граница
        right = min(rect_1[1][0], rect_2[1][0])  # правая граница
        upper = min(rect_1[1][1], rect_2[1][1])    # верхняя граница
    width = right - left
    height = upper - lower
    square=0
    if width < -10 or height < -10:
        raise ("Некорректные размеры прямоугольника")
    elif width <= 0 or height <= 0:
        print(0)  #пересечений нет
    else:
        square=width * height
        print(square)  # площадь пересечения
