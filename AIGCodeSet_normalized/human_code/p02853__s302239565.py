v1, v2 = map(int, input().split())
v3 = 0
if v1 == 3:
    v3 += 100000
elif v1 == 2:
    v3 += 200000
elif v1 == 1:
    v3 += 300000
if v2 == 3:
    v3 += 100000
elif v2 == 2:
    v3 += 200000
elif v2 == 1:
    v3 += 300000
if v1 == 1 and v2 == 1:
    v3 += 400000
print(v3)
