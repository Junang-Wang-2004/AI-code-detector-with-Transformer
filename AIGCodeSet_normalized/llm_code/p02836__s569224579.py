v1 = input()
v2 = 0
if len(v1) % 2 == 0:
    for v3 in range(len(v1) // 2):
        if v1[v3] != v1[len(v1) - 1 - v3]:
            v2 += 1
else:
    for v3 in range((len(v1) + 1) // 2):
        if v1[v3] != v1[len(v1) - 1 - v3]:
            v2 += 1
print(v2)
