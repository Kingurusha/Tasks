x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if x and y and x1 and y1 > 0:
    print("YES")
elif x and x1 < 0 and y and y1 > 0:
    print("YES")
elif x and x1 < 0 and y and y1 < 0:
    print("YES")
elif x and x1 > 0 and y and y1 < 0:
    print("YES")
else:
    print("NO")
