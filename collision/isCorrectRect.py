def isCorrectRect(coordinates):
    left_c,right_c=coordinates
    x_left, y_left=left_c
    x_right,y_right=right_c
    if not isinstance(coordinates,list) or len(coordinates)!=2:
        return False
    elif not (isinstance(x_left, (int, float)) and isinstance(y_left, (int, float)) and isinstance(x_right, (int, float)) and isinstance(y_right, (int, float))):
        return False
        
    elif ((x_left > x_right) or (y_left > y_right)):
        return False
    elif not all(isinstance(coord_pair, tuple) and len(coord_pair) == 2 for coord_pair in coordinates):
        return False
    return True