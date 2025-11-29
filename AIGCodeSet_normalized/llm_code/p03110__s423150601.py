v1 = int(input())
v2 = [input().split() for v3 in range(v1)]
v4 = 0
for v3 in v2:
    if v3[1] == 'JPY':
        v4 += int(v3[0])
    else:
        v4 += int(float(v3[0]) * 380000)
print(v4)
