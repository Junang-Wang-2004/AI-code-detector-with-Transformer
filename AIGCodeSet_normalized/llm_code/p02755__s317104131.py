v1 = int(input())
v2 = int(input())
v3 = math.floor(v1 / 0.08)
v4 = math.floor(v2 / 0.1)
if v3 != v4:
    print(-1)
else:
    print(v3)
