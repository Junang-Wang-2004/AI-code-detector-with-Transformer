v1 = input()
v2 = []
v3 = []
v4 = 0
for v5 in list(v1):
    if v5 != 'x':
        v3.append(v4)
        v2.append(v5)
    v4 += 1
if v2 != v2[::-1]:
    print(-1)
else:
    print(v3[len(v3) // 2])
