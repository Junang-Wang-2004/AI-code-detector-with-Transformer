v1, v2 = map(int, input().split())
v3 = set()
for v4 in range(v2):
    v3.add(int(input()))
v5 = [0] * (v1 + 1)
v5[0] = 1
v5[1] = 1
for v6 in range(2, v1 + 1):
    if v6 in v3:
        continue
    v5[v6] = (v5[v6 - 1] + v5[v6 - 2]) % 1000000007
print(v5[v1])
