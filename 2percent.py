a = int(input())  # процентная ставка годовых
b = int(input())  # рублей
c = int(input())  # копеек
anuual = (b / 100) * a + b
ruble = float(b) / a + b
kopecks = float(c) / a
kopeck = c + kopecks
print(int(ruble), '', int(kopeck))
