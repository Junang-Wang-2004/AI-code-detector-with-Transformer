from math import floor
v1 = int(input())
v2 = 50
v3 = list(range(v2))
v4 = floor(v1 / v2)
v5 = v1 % v2
v3 = list(map(lambda x: x + v4, v3))
for v6 in range(v5):
    v3[v6] += v2
    for v7 in range(v2):
        if v7 != v6:
            v3[v7] -= 1
print(v2)
print(' '.join(map(str, v3)))
