x = float(input())
y = float(input())
c = 1
while x < y:
    x = (x * 0.1) + x
    c += 1
print(c)
