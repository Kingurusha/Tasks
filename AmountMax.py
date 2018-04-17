maxeven = []
a = 1
while a != 0:
    a = int(input())
    maxeven.append(a)
maxeven.sort()
maxeven.remove(0)
print(maxeven[-2])
