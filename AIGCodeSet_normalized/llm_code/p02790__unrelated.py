v1, v2 = map(int, input().split())
if int(str(v1) * v2) < int(str(v2) * v1):
    print(str(v1) * v2)
else:
    print(str(v2) * v1)
