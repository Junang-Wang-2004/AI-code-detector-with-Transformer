v1 = int(input())
v2 = []
v3 = 0
for v4 in range(1, v1):
    if v3 >= v1:
        break
    v2.append(v4)
    v3 += v4
if v3 == v1:
    print(*v2)
else:
    v2.pop(v3 - v1)
    print(*v2)
