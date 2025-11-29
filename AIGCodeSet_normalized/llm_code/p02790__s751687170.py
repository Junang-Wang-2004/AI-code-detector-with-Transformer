v1, v2 = map(int, input().split())
v3 = int(str(v1) * v2)
v4 = int(str(v2) * v1)
if v3 <= v4:
    print(v4)
else:
    print(v3)
