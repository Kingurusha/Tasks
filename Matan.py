import math
a = float(input())
b = float(input())
c = float(input())
D = b * b - 4 * a * c
if D > 0:
    D = math.sqrt(D)
    X1 = (-b - D) / (2 * a)
    X2 = (-b + D) / (2 * a)
    if X1 > X2:
        print(X2, '', X1)
    else:
        print(X1, '', X2)
elif D == 0:
    D = math.sqrt(D)
    X1 = -b / (2 * a)
    print(X1)
