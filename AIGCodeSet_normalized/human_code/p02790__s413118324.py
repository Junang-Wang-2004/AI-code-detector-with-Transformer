v1, v2 = map(int, input().split())
v3 = []
v4 = []
if v2 <= v1:
    for v5 in range(v1):
        v3.append(v2)
else:
    for v5 in range(v2):
        v4.append(v1)
if v2 <= v1:
    v3 = int(''.join(map(str, v3)))
    print(v3)
else:
    v4 = int(''.join(map(str, v4)))
    print(v4)
