v1, v2, v3 = map(int, input().split())
if v1 % v3 == 0:
    min = v1 // v3 - 1
else:
    min = v1 // v3
max = v2 // v3
print(max - min)
