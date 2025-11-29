v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
v5 = 0
for v6 in range(v1):
    for v7 in range(v6):
        if v2[v6] > v2[v7]:
            v8 = int(scipy.special.comb(v2[v6], v2[v7], exact=True))
            if v8 > v5:
                v5 = v8
                v3 = v2[v6]
                v4 = v2[v7]
print(v3, v4)
