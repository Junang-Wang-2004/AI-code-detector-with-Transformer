v1 = int(input())
v2 = list(map(int, input().split()))
v2 = sorted(v2)
print(v2[v1 // 2] - v2[v1 // 2 - 1])
