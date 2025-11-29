v1, v2, v3, v4 = map(int, input().split())
if int(v1) >= int(v4):
    print(int(v4))
elif int(v1 + v2) >= int(v4):
    print(int(v1 + v2))
else:
    print(int(v1 + v2 - (v4 - v1 - v2)))
