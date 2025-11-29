v1 = int(input())
v2 = [0] * v1 * v1

def f1(a1, a2):
    if a1 < a2:
        v2[(a1 - 1) * v1 + (a2 - 1)] = 1
    else:
        v2[(a2 - 1) * v1 + (a1 - 1)] = 1
if v1 % 2 == 0:
    v3 = v1 + 1
else:
    v3 = v1
for v4 in range(v1):
    for v5 in range(v4):
        if v4 + 1 + v5 + 1 != v3:
            v2[v5 * v1 + v4] = 1
v6 = 0
for v4 in range(v1 * v1):
    if v2[v4] == 1:
        v6 += 1
print(v6)
for v4 in range(v1 * v1):
    if v2[v4] == 1:
        v7 = v4 // v1
        v8 = v4 % v1
        print(str(v7 + 1) + ' ' + str(v8 + 1))
