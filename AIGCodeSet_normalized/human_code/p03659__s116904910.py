v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * (v1 + 1)
for v4 in range(v1):
    v3[v4 + 1] = v3[v4] + v2[v4]
v5 = 10 ** 18
v6 = v5
for v4 in range(1, v1):
    v6 = min(v6, abs(v3[v4] - (v3[-1] - v3[v4])))
print(v6)
