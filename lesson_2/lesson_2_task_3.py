import math

def square(a):
    b = a * a
    
    if not isinstance(a, int):
        b = math.ceil(b)
    
    return b

a_length = 2.5
b = square(a_length)

print(f"Площадь квадрата со стороной {a_length} равна: {b}")