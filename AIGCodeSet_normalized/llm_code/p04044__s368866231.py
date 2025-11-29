v1, v2 = map(int, input().split())
v3 = [input() for v4 in range(v1)]
v3.sort()
v5 = ''.join(v3)
print(v5)
