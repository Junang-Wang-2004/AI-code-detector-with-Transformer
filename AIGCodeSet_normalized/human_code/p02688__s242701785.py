v1, v2 = map(int, input().split())
v3 = [0] * v1
v4 = []
for v5 in range(v1):
    v3[v5] += v5 + 1
for v5 in range(v2):
    v6 = input()
    v4 += input().split()
v7 = [int(s) for v8 in v4]
v9 = set(v3) ^ set(v7)
print(len(v9))
