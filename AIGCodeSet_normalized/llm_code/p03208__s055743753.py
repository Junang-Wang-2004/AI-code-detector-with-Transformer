v1, v2 = map(int, input().split())
v3 = [int(input()) for v4 in range(v1)]
v3.sort()
v5 = 10 ** 9
for v4 in range(v1 - v2 + 1):
    if v3[v4 + v2 - 1] - v3[v4] < v5:
        v5 = v3[v4 + v2 - 1] - v3[v4]
print(v5)
