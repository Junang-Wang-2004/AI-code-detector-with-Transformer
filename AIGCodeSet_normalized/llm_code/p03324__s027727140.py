v1, v2 = map(int, input().split())
v3 = 0
if v1 == 0:
    v3 = v2
elif v1 == 1:
    v3 = v2 * 100
elif v1 == 2:
    v3 = v2 * 10000
print(v3)
