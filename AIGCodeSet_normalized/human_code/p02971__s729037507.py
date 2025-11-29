v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = [v2[v3] for v3 in range(v1)]
v4.sort()
v5 = v4[v1 - 1]
v6 = v4[v1 - 2]
for v3 in range(v1):
    if v2[v3] == v5:
        print(v6)
    else:
        print(v5)
