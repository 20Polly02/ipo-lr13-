class RectCorrectError(Exception):
    pass
from .isCorrectRect import isCorrectRect

def isCollisionRect(list_1,list_2):
    rect_1, rect_2 = list_1, list_2
    if not isCorrectRect(rect_1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect_2):
        raise RectCorrectError("2й прямоугольник некоректный")
    else:
        (x1,y1),(x2,y2) = rect_1
        (x3,y3),(x4,y4) = rect_2
    if (x2<x3 or x1>x4 or y1>y4 or y2<y3):
        return False
    return True