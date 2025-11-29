v1 = int(input())
v2 = [[0] * 3] * v1
for v3 in range(v1):
    v4 = list(map(int, input().split()))
    if v3 == 0:
        v2[v3] = v4
    else:
        v5 = v2[v3 - 1]
        v6 = []
        for v7 in range(3):
            v8 = v5[1:3]
            v6.append(max(v8) + v4[v7])
            v5.append(v5[0])
            del v5[0]
        v2[v3] = v6
print(max(v2[-1]))
