v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sum((v2[x] % 2 for v4 in range(0, v1, 2)))
print(v3)
