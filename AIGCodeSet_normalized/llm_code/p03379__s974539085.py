import copy
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * max(v2)
for v4 in range(v1):
    if v3[v2[v4] - 1] > 0:
        print(v3[v2[v4] - 1])
    else:
        v5 = copy.copy(v2)
        v5.pop(v4)
        v5.sort()
        v6 = v5[v1 // 2 - 1]
        print(v6)
        v3[v2[v4] - 1] = v6
