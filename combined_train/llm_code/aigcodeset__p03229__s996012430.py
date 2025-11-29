import collections
v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v2 = sorted(v2)
v4 = collections.deque()
v4.append(v2[0])
v5 = 1
v6 = v1 - 1
v7 = 1
if v1 % 2 == 1:
    while 1:
        v4.appendleft(v2[v6])
        v6 -= 1
        v4.append(v2[v6])
        v6 -= 1
        v7 += 2
        if v7 == v1:
            break
        v4.appendleft(v2[v5])
        v5 += 1
        v4.append(v2[v5])
        v5 += 1
        v7 += 2
        if v7 == v1:
            break
    v4 = list(v4)
    v8 = 0
    for v9 in range(v1 - 1):
        v8 += abs(v4[v9 + 1] - v4[v9])
    print(v8)
else:
    v10 = 0
    while 1:
        if v1 - v7 == 1:
            v10 = 0
            break
        v4.appendleft(v2[v6])
        v6 -= 1
        v4.append(v2[v6])
        v6 -= 1
        v7 += 2
        if v1 - v7 == 1:
            v10 = 1
            break
        v4.appendleft(v2[v5])
        v5 += 1
        v4.append(v2[v5])
        v5 += 1
        v7 += 2
    v4 = list(v4)
    v8 = 0
    for v9 in range(v1 - 2):
        v8 += abs(v4[v9 + 1] - v4[v9])
    v8 += max(abs(v2[v5] - v4[0]), abs(v2[v5] - v4[-1]))
    print(v8)
