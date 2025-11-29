v1, v2, v3 = map(int, input().split(' '))
if v1 >= v3:
    v1 -= v3
else:
    v3 -= v1
    v1 = 0
    v2 = max(v2 - v3, 0)
print(str(v1) + ' ' + str(v2))
