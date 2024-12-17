def isCorrectRect():
    left_lower= (-7, 9)  # Координаты первой точки
    right_upper= (3, 6)   # Координаты второй точки

    # Проверяем условия корректности
    if left_lower[0] > right_upper[0] or left_lower[1] > right_upper[1]:
        print("False")  # Некорректный прямоугольник
    else:
        print("True")   # Корректный прямоугольник
