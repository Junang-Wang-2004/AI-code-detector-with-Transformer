v1 = list(map(int, input().split()))
v2 = False
v3 = False
if max(v1[0], v1[1]) < 0:
    v2 = True
if max(v1[2], v1[3]) < 0:
    v3 = True
if v2 and v3:
    v4 = v1[0] * v1[2]
elif v2:
    v4 = v1[0] * v1[3]
elif v3:
    v4 = v1[1] * v1[2]
else:
    v4 = v1[1] * v1[3]
print(v4)
