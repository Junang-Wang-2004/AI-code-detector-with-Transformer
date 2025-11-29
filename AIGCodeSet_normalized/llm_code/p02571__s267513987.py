v1 = input()
v2 = input()
v3 = 0
for v4 in range(len(v1) - len(v2) + 1):
    for v5 in range(len(v2)):
        if v1[v4 + v5] != v2[v5]:
            break
    else:
        v3 = len(v2)
        break
print(len(v2) - v3)
