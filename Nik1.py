print("Введите число")
number = int(input())
newNumber = 0

for item in range(0, number // 9):
    newNumber += 9 * 10 ** item
    print("Новое число: " + str(newNumber) + " Шаг: " + str(item))

newNumber += (number % 9) * (10 ** (number // 9))
print(newNumber)