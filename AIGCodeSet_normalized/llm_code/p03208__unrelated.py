v1, v2 = map(int, input().split())
v3 = [int(input()) for v4 in range(v1)]
v3.sort()
print(v3[v2 - 1] - v3[0])
