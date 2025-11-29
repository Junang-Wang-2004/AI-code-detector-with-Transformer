v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(max(v2)):
    v5 = False
    for v6 in range(v1):
        if v2[v6] > 0:
            v2[v6] -= 1
            if not v5:
                v3 += 1
                v5 = True
        elif v2[v6] == 0:
            v5 = False
print(v3)
