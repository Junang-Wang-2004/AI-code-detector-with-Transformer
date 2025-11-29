v1 = int(input())
v2 = 0
if 400 <= v1 <= 599:
    v2 = 8
elif 600 <= v1 <= 799:
    v2 = 7
elif 800 <= v1 <= 999:
    v2 = 6
elif 1000 <= v1 <= 1199:
    v2 = 5
elif 1200 <= v1 <= 1399:
    v2 = 4
elif 1400 <= v1 <= 1599:
    v2 = 3
elif 1600 <= v1 <= 1799:
    v2 = 2
elif 1800 <= v1 <= 1999:
    v2 = 1
print(v2)
