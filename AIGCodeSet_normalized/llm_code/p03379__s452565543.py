v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
for v3 in range(v1):
    if v3 < v1 // 2:
        print(v2[v1 // 2])
    else:
        print(v2[v1 // 2 - 1])
