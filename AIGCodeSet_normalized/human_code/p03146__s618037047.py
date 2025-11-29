v1 = int(input())
v2 = v1
v3 = [v2]
while True:
    if v1 % 2 == 0:
        v1 = v1 // 2
    else:
        v1 = 3 * v1 + 1
    if v1 in v3:
        break
    v3.append(v1)
print(len(v3) + 1)
