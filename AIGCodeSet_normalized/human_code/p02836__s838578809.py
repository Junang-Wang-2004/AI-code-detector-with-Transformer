v1 = list(str(input()))
v2 = v1[:len(v1) // 2]
v3 = list(reversed(v1))[:len(v1) // 2]
v4 = 0
for v5, v6 in zip(v2, v3):
    if v5 == v6:
        pass
    else:
        v4 += 1
print(v4)
