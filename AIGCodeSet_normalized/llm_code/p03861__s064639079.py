v1, v2, v3 = map(int, input().split())
v4 = 0
if v1 == 0:
    v4 = 1
print(int((v2 - v1) // v3 + v4))
