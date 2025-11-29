import sys
input = sys.stdin.readline
v1 = input().strip()
v2 = int(input())
v3 = []
v4 = v1[0]
v5 = 1
if len(v1) == 1:
    print(v2 // 2)
    exit()
v6 = True
for v7 in range(len(v1) - 1):
    if v1[v7] != v1[v7 + 1]:
        v6 = False
if v6:
    print(len(v1) * v2 // 2)
    exit()
v6 = True
v8 = v1 + v1[0]
for v7 in range(len(v8) - 1):
    if v8[v7] == v8[v7 + 1]:
        v6 = False
if v6:
    print(0)
    exit()
for v7 in range(1, len(v1)):
    v9 = v1[v7]
    if v4 == v9:
        v5 += 1
    else:
        if v5 >= 2:
            v3.append(v5 // 2)
        v5 = 1
    v4 = v9
if v5 >= 2:
    v3.append(v5 // 2)
v10 = 1
for v7 in range(len(v1) - 1):
    if v1[v7] == v1[v7 + 1]:
        v10 += 1
    else:
        break
if (v5 + v10) % 2 == 0:
    v11 = True
else:
    v11 = False
if v1[0] == v1[-1] and v11:
    v3.append(1)
    v11 = True
else:
    v11 = False
v12 = sum(v3) * v2
if v11:
    v12 -= 1
print(v12)
