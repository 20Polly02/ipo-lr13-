from .isCorrectRect import isCorrectRect
class RectCorrectError(Exception):
    pass
def isCollisionRect(list_1,list_2):
    rect_1, rect_2 = list_1, list_2
    if not isCorrectRect(rect_1):
        raise RectCorrectError("Первый прямоугольник некоректный")
    if not isCorrectRect(rect_2):
        raise RectCorrectError("Второй прямоугольник некоректный")
    else:
        (x1,y1),(x2,y2) = rect_1
        (x3,y3),(x4,y4) = rect_2
    if (x2<x3 or x1>x4 or y1>y4 or y2<y3):
        return False
    return True
