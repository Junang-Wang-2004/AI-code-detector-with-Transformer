v1 = [str(e) for v2 in input().split()]
if v1[1] == '+':
    v3 = int(v1[0]) + int(v1[2])
else:
    v3 = int(v1[0]) - int(v1[2])
print(v3)
