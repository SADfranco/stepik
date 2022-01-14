figure = str(input())
if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c))**(0.5)
    print(float(S))
elif figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)   
elif figure == 'круг':
    a = int(input())
    print(3.14 * a ** 2)