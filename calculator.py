def add (x,y):
    max_decimal_length = [0]
    if (type(x) == float):
        max_decimal_length.append(len(repr(x).split('.')[-1]))
    if (type(y) == float):
        max_decimal_length.append(len(repr(y).split('.')[-1]))
    return round(x + y,max(max_decimal_length))
    