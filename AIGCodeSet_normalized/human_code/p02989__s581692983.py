v1 = int(input())
v2 = sorted(list(map(int, input().split())))
v3 = v2[v1 // 2]
v4 = v2[v1 // 2 - 1]
print(v3 - v4 if v3 > v4 else 0)
