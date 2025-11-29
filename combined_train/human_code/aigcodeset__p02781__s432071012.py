from math import factorial

def f1(a1, a2):
    if a1 >= a2:
        return int(factorial(a1) / (factorial(a2) * factorial(a1 - a2)))
    else:
        return 0

def f2(a1, a2):
    v1 = len(a1)
    v2 = len(a1) - 1
    if a2 < 1 or v1 == 0:
        return 0
    else:
        if a1[v2] > 0:
            v3 = 9 ** a2 * f1(v2, a2) + 9 ** (a2 - 1) * (a1[v2] - 1) * f1(v2, a2 - 1)
            v3 += f2(a1[:v1 - 1], a2 - 1)
        else:
            v3 = 0
            v3 += f2(a1[:v1 - 1], a2)
        if a1[-a2] >= 1 and a2 == 1:
            v3 += 1
        return v3
v1 = int(input())
v2 = int(input())
v3 = []
while v1:
    v3.append(v1 % 10)
    v1 //= 10
v4 = len(v3)
v5 = len(v3) - 1
if v4 >= v2:
    v6 = 0
    v6 += f2(v3, v2)
else:
    v6 = 0
print(v6)
