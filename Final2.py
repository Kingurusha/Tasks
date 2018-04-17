maxCount = 0
Count = -1
a = int(input())
b = 0
while a != 0:
    if Count == a:
        b += 1
    else:
        Count = a
        maxCount = max(maxCount, b)
        b = 1
    a = int(input())
maxCount = max(maxCount, b)
print(maxCount)
