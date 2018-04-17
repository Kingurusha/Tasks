N = int(input())
second = N % 60
minutes = (N // 60) % 60
hours = (N // 60) // 60
if minutes < 10 and second < 10:
    print(hours, ':', '0', minutes, ':', '0', second, sep='')
elif minutes < 10 and second > 10:
    print(hours, ':', '0', minutes, ':', second, sep='')
elif minutes > 10 and second < 10:
    print(hours, ':', minutes, ':', '0', second, sep='')
elif minutes > 10 and second > 10:
    print(hours, ':', minutes, ':', second, sep='')
