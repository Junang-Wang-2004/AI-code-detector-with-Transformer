v1 = int(input())
v2 = v1 // 3
v3 = v1 % 3
if v3 == 1:
    v2 -= 1
elif v3 == 2:
    v2 += 1
print(v2)
