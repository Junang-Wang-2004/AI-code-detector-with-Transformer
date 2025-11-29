v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = sorted(v2, reverse=True)
v5 = v4[0]
v6 = v4[1]
for v3 in range(v1):
    if v2[v3] == v5:
        print(v6)
    else:
        print(v5)
