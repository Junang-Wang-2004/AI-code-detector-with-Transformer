v1, v2 = map(int, input().split())
v3 = [1] * (v1 + 1)
v4 = 1000000000.0 + 7
for v5 in range(v2):
    v3[int(input())] = 0
v6 = [1] * (v1 + 1)
if v3[1] == 0:
    v6[1] = 0
for v5 in range(2, v1 + 1):
    v6[v5] = int(v3[v5] * (v6[v5 - 2] + v6[v5 - 1]) % v4)
print(v6[v1])
