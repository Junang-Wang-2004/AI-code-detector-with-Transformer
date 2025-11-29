v1 = list(input())
v2 = v1[:]
for v3 in range(len(v1)):
    if len(v2) == 1:
        break
    v2.pop()
    if len(v2) % 2 == 0:
        v4 = len(v2) // 2
        if v2[:v4] == v2[v4:]:
            break
if len(v2) == 1:
    print(-1)
else:
    print(len(v2))
