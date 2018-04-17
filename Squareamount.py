a = int(input())
now = 0
while a != 0:
    square = now + a ** 2
    now = square
    a -= 1
print(square)
