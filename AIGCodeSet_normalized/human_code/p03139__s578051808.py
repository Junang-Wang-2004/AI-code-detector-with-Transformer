v1, v2, v3 = map(int, input().split())
if v2 > v3:
    v2, v3 = (v3, v2)
max = v2
if v2 + v3 < v1:
    min = 0
else:
    min = v2 + v3 - v1
print(max, min)
