class RectCorrectError(Exception):
    pass


def isCollisionRect():
    rectangle_1 = [(-3.4, 1), (9.2, 10)]    # Первый прямоугольник
    rectangle_2 = [(-7.4, 0), (13.2, 12)]  # Второй прямоугольник

    # Координаты прямоугольников
    x1_r1, y1_r1 = rectangle_1[0]
    x2_r1, y2_r1 = rectangle_1[1]
    x1_r2, y1_r2 = rectangle_2[0]
    x2_r2, y2_r2 = rectangle_2[1]

    # Проверка пересечения по оси Y
    if y2_r1 < y1_r2 or y2_r2 < y1_r1:
        raise RectCorrectError("Некорректный прямоугольник")  # Ошибка

    # Проверка пересечения по оси X
    elif x2_r1 < x1_r2 or x2_r2 < x1_r1:
        print("False")  # Нет пересечения

    else:
        print("True")   # Есть пересечение
