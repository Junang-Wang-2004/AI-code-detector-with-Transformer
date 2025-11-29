v1 = [x for v2 in input()]
if v1[1] < v1[2]:
    v1[1] = str(int(v1[1]) + 1)
if v1[0] < v1[1]:
    v1[0] = str(int(v1[0]) + 1)
print(v1[0] * 3)
