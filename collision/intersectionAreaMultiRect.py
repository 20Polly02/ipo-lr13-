class RectCorrectError(Exception):
    pass
from .isCorrectRect import isCorrectRect
def intersectionAreaMultiRect(rects_coords):
    uniq_c = []
    for num_rect, rect in enumerate(rects_coords, start=1):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Прямоугольник {num_rect} некорректный")
        
        if rect not in uniq_c:
            uniq_c.append(rect)
    total_square = 0
    list_len = len(uniq_c)
    for i in range(list_len):
        for j in range(i + 1, list_len):
            (x1, y1), (x2, y2) = uniq_c[i]
            (x3, y3), (x4, y4) = uniq_c[j]
            if x1 > x4 or y1 > y4 or x2 < x3 or y2 < y3:
                continue
            x_left = max(x1, x3)
            y_lower = max(y1, y3)
            x_right = min(x2, x4)
            y_upper = min(y2, y4)

            width = x_right - x_left
            height = y_upper - y_lower

            if width > 0 and height > 0:  
                total_square += width * height
   return total_square
