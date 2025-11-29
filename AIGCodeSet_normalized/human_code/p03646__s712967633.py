import heapq
v1 = int(input())
v2 = [49] * 50
for v3 in range(50):
    v2[v3] += v1 // 50
v1 %= 50
for v3 in range(v1):
    for v4 in range(50):
        if v3 == v4:
            v2[v4] += v1
        else:
            v2[v4] -= 1
print(len(v2))
print(' '.join(list(map(str, v2))))
