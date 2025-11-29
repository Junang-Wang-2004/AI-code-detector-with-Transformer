v1 = int(input())
v2 = 0
v3 = 0
while v3 != v1:
    v2 += 1
    v3 += v2
    if v3 > v1:
        v4 = v3 - v1
        if v4 % 2 == 0:
            break
print(v2)
