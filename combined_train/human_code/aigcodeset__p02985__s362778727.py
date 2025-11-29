import collections
v1, v2 = map(int, input().split())
v3 = [set() for v4 in range(v1)]
for v4 in range(v1 - 1):
    v5, v6 = map(int, input().split())
    v5 -= 1
    v6 -= 1
    v3[v5].add(v6)
    v3[v6].add(v5)
v7 = 0
id = 9
for v4 in range(v1):
    if len(v3[v4]) > v7:
        id = v4
        v7 = len(v3[v4])
v8 = collections.deque()
v8.append(0)
v9 = [False] * v1
v9[0] = True
from math import factorial
v10 = 10 ** 9 + 7
v11 = v2
while v8:
    v12 = v8.popleft()
    v13 = 0
    for v14 in v3[v12]:
        if v9[v14]:
            continue
        else:
            v8.append(v14)
            v9[v14] = True
            v13 += 1
    for v4 in range(v13):
        v11 *= v2 - 1 - (len(v3[v12]) - v13) - v4
        v11 %= v10
print(v11)
