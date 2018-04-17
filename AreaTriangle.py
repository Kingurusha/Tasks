import math

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2
Geroin = (p - a) * (p - b) * (p - c)
S = math.sqrt(p * Geroin)

print(S)
