v1 = int(input())
v2 = [ai - i for v3, v4 in enumerate(map(int, input().split()), 1)]
v2.sort()
v5 = v2[len(v2) // 2]
print(sum((abs(v4 - v5) for v4 in v2)))
