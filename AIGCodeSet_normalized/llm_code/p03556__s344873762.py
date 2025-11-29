v1 = int(input())
v2 = 0
for v3 in range(1, v1 // 2):
    next = v3 ** 2
    if next <= v1:
        v2 = v3 ** 2
    else:
        break
print(v2)
