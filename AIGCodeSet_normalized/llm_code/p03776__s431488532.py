v1 = list(map(int, input().split(' ')))
v2 = v1[0]
v3 = v1[1]
v4 = v1[2]
v5 = list(map(int, input().split(' ')))
v5.sort(reverse=True)
v6 = sum(v5[:v3]) / v3
v7 = 0
v8 = 0
for v9 in range(v2):
    if v5[v9] == v5[v3 - 1]:
        v7 += 1
        if v9 < v3:
            v8 += 1
import math

def f1(a1, a2):
    v1 = math.factorial
    return v1(a1) / v1(a2) / v1(a1 - a2)
v10 = 0
if v8 == v3:
    while v8 <= v4:
        v10 += f1(v7, v8)
        v8 += 1
else:
    v10 = f1(v7, v8)
print('{0:.6f}'.format(v6))
print(int(v10))
