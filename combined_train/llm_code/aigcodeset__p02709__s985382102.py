import math
v1 = int(input())
v2 = list(map(int, input().split()))
list = [0 for v3 in range(v1)]
v4 = 0
sum = 0
for v3 in list:
    if v3 == 1:
        continue
    max = [0, 0, 0]
    for v5 in range(v1):
        if v5 == v4 or list[v5] == 1:
            continue
        v6 = (v2[v4] + v2[v5]) * abs(v4 - v5)
        if v6 > max[0]:
            max = [v6, v5, v4]
    sum += max[0]
    list[max[1]] = 1
    list[max[2]] = 1
    v4 += 1
print(sum)
