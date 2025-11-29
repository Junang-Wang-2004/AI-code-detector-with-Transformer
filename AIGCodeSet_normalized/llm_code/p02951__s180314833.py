v1 = input().split(' ')
for v2 in range(3):
    v1[v2] = int(v1[v2])
v3 = v1[2] - (v1[0] - v1[1])
if v3 < 0:
    print(0)
else:
    print(v3)
