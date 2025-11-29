v1 = int(input())
v2 = [int(x) for v3 in input().split()]
for v4 in range(v1):
    v5 = v2[v4]
    del v2[v4]
    print(max(v2))
    v2.insert(v4, v5)
