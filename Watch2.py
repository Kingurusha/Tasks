N = int(input())
second = N % 60
minutes = (N // 60) % 60
hours = (N // 60) // 60
print (hours,':',minutes,':',second, sep = '')
