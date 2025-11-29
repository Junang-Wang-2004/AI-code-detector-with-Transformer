from heapq import heappush, heappop
v1 = int(input())
v2, v3 = zip(*(map(int, input().split()) for v4 in range(v1 - 1))) if v1 - 1 else ((), ())
v5 = list(map(int, input().split()))
v6 = 10 ** 10
v7 = [{} for v4 in range(v1 + 1)]
for v8, v9 in zip(v2, v3):
    v7[v8][v9] = 1
    v7[v9][v8] = 1

def f1(a1, a2):
    v1 = [v6 for v4 in range(len(a1))]
    v2 = []
    heappush(v2, (0, a2))
    while v2:
        v3, v4 = heappop(v2)
        if v1[v4] == v6:
            v1[v4] = v3
            for v5, v6 in a1[v4].items():
                heappush(v2, (v3 + v6, v5))
    return v1
v10 = f1(v7, 1)
v11 = dict()
for v8, (v4, v12) in zip(sorted(v5), sorted(zip(v10[1:], range(1, v1 + 1)), reverse=True)):
    v11[v12] = v8
v13 = 0
for v8, v9 in zip(v2, v3):
    v13 += min(v11[v8], v11[v9])
print(v13)
v14 = ' '.join((str(v11[i]) for v15 in range(1, v1 + 1)))
print(v14)
