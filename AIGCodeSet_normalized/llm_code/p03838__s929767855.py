v1, v2 = map(int, input().split())
if v1 == v2:
    v3 = 0
elif v2 > v1:
    if v1 <= 0 and v2 >= 0 and ((v1 + v2) // 2 >= 0):
        v3 = v2 - abs(v1) + 1
    else:
        v3 = v2 - v1
elif v1 > v2:
    if v2 >= 0:
        v3 = v1 - v2
    elif v1 <= 0:
        v3 = abs(v2) - abs(v1) + 2
    else:
        v3 = abs(abs(v1) - abs(v2)) + 1
print(v3)
