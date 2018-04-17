a = float(input())
b = 2
c = 3
d = 0
if a == 1.0:
    print("1")
else:
    d = (1 / 2 ** 2)
    while b != a:
        d += (1 / c ** 2)
        c += 1
        b += 1
    print(d + 1)
