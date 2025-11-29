v1 = input()
v2 = int(v1) % 111
if v2 == 0:
    print(v1)
elif v1[0] > v1[1] or (v1[0] == v1[1] and v1[1] > v1[2]):
    print(v1[0] * 3)
else:
    print(str(int(v1[0]) + 1) * 3)
