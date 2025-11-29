v1, v2, v3 = map(int, input().split())
if v3 >= v1 + v2:
    v1 = 0
    v2 = 0
elif v3 >= v1:
    v2 = v2 - (v3 - v1)
    v1 = 0
else:
    v1 = v1 - v3
    v2 = v2
print(v1, v2)
