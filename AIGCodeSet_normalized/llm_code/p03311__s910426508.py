from statistics import mode
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(lambda e: e[1] - (e[0] + 1), enumerate(v2)))
v4 = mode(v3)
v5 = sum(map(lambda ea: abs(ea - v4), v3))
print(v5)
