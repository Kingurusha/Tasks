a = int(input())
b = int(input())
step = b - (a - 1)
if (a - 1) % int(step) == 0:
    print('YES')
else:
    print('NO')
