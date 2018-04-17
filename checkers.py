a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a + b) % 2 == 0 and (c + d) % 2 == 0:
    if (b < d) and (a <= c):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
