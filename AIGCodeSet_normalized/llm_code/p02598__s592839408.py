import math
v1, v2 = map(int, input().split())
v3 = sorted(list(map(int, input().split())), reverse=True)
v4 = 0
v5 = v3[0]
while v4 != v5:
    v6 = (v4 + v5) // 2
    v7 = 0
    for v8 in v3:
        v7 += (v8 + v6 - 1) // v6 - 1
    if v7 > v2:
        v4 = v6 + 1
    else:
        v5 = v6
print(v4)
