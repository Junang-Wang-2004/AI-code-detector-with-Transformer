v1 = int(input())
v2 = {}
v2[v1] = True
v3 = 1
while True:
    v3 += 1
    if v1 % 2 == 1:
        v1 = v1 * 3 + 1
    else:
        v1 = v1 // 2
    if v2.get(v1):
        break
    else:
        v2[v1] = True
print(v3)
