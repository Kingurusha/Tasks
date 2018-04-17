import math
a = int(input())  # процентная ставка годовых
b = int(input())  # рублей
c = int(input())  # копеек
anuual = (b / 100) * a + b
copecs = c * (a / 100) + c
ostatoc = anuual - math.floor(anuual)
anuuals = (ostatoc + copecs) / 100
anuuals1 = anuual + anuuals
secon = anuuals1 - math.floor(anuuals1)
if c == 0:
    print(math.floor(anuuals1), '', (int(secon * 100)))
else:
    print(math.floor(anuuals1), '', 1 + (int(secon * 100)))
