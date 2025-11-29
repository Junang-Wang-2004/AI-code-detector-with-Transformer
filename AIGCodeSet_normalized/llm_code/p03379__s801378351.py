v1 = int(input())
v2 = list(map(int, input().split()))
v3 = int(v1 / 2)
for v4 in range(v1):
    v5 = []
    for v6 in range(v1):
        if v6 != v4:
            v5.append(v2[v6])
    v5.sort()
    print(v5[v3 - 1])
