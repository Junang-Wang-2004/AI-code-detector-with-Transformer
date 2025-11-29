v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7
from collections import deque
v4 = list(map(int, input().split()))
v4.sort()
v5, v6, v7 = (0, 0, 0)
for v8 in range(v1):
    if v4[v8] < 0:
        v5 += 1
    elif v4[v8] == 0:
        v6 += 1
    else:
        v7 += 1
v9 = deque(v4)
v10 = False
v11 = v7 - v2
if v11 >= 0:
    v10 = True
elif -v11 <= v5 and (-v11 % 2 == 0 or v11 > 0):
    v10 = True
if v10:
    v12 = 1
    v13 = 0
    while v13 < v2:
        if v2 - v13 >= 2:
            v13 += 2
            if v9[0] * v9[1] >= v9[-1] * v9[-2]:
                v12 *= v9.popleft()
                v12 *= v9.popleft()
                v12 %= v3
            else:
                v12 *= v9.pop()
                v12 *= v9.pop()
                v12 %= v3
        else:
            v12 *= v9.pop()
            v12 %= v3
            v13 += 1
    print(v12)
elif v6 > 0:
    print(0)
else:
    v4 = [abs(v4[v8]) for v8 in range(v1)]
    v4.sort()
    v12 = 1
    for v8 in range(v2):
        v12 *= v4[v8]
        v12 %= v3
    v12 = -v12 % v3
    print(v12)
