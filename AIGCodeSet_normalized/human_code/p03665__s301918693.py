v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [x % 2 for v5 in v3]
if 1 in v4:
    v6 = 2 ** (v1 - 1)
elif v2 == 0:
    v6 = 2 ** v1
else:
    v6 = 0
print(v6)
