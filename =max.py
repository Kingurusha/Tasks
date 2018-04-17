number = []
a = 1
while a != 0:
    a = int(input())
    number.append(a)
number.remove(0)
number.sort()
c = number[-1]
number.count(c)
print(number.count(c))
