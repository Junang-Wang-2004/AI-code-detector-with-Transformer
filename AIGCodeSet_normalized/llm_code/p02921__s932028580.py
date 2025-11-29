v1 = list(input())
v2 = list(input())
v3 = 0
for v4 in range(len(v1)):
    if v1[v4] == v2[v4]:
        v3 += 1
print(v3)
print(v1, v2)
