import math

a = float(input())
b = a - int(a)
if b == 0.5:
    print(math.ceil(a))
elif b < 0.5:
    print(math.floor(a))
else:
    print(math.ceil(a))
