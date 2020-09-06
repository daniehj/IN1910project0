def add (x,y):
    max_decimal_length = [0]
    if (type(x) == float):
        max_decimal_length.append(len(repr(x).split('.')[-1]))
    if (type(y) == float):
        max_decimal_length.append(len(repr(y).split('.')[-1]))
    if ((type(x) == str) and (type(y)==str)):
        return x + y

    return round(x + y,max(max_decimal_length))
    
def factorial(n):
    result = 1
    number_list = [i for i in range(1,n+1)]
    for x in number_list:
        result = result*x
    return result

def sin(x,N):
    return sum([(((-1)**n)*(x**(2*n+1)))/(factorial(2*n+1)) for n in range(0,N+1)])

def divide(x,y):
    return float(x)/float(y)
