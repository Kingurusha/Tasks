a = int(input())
b = int(input())
c = int(input())
total = c % a and c % b
if int(total) == 0 and (a * b) > c:
    print("YES")
else:
    print("NO")
