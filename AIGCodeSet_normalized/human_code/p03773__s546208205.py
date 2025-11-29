v1, v2 = map(int, input().split())
v3 = v1 + v2
if v3 >= 24:
    v3 = v3 - 24
print(v3)
