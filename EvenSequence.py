a = int(input())
lens = 0
while a != 0:
    if a % 2 == 0:
        lens += 1
    a = int(input())
print(lens)
