v1, v2 = list(map(int, input().split()))
v3 = [input() for v4 in range(v2)]
v3.sort()
v5 = ''
for v6 in range(v2):
    v5 += v3[v6]
print(v5)
