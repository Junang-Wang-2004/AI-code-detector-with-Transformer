v1 = input()
for v2 in range(1, len(v1) - 1):
    v1 = v1[:-2]
    if v1[:len(v1) // 2] == v1[len(v1) // 2:]:
        break
print(len(v1))
