v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [0, 0]
for v5 in v3:
    v4[v5 % 2] += 1
if 0 == v4[1]:
    print(2 ** v1 * ((v2 + 1) % 2))
else:
    print(2 ** (v1 - 1))
