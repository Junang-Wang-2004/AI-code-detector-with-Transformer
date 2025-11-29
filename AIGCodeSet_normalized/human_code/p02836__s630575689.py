v1 = input()
v2 = v1[::-1]
v3 = 0
for v4 in range(len(v1)):
    if v1[v4] != v2[v4]:
        v3 += 1
print(int(v3 / 2))
