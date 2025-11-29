v1 = int(input())
v2 = input()
v3 = [0]
for v4 in range(v1):
    if v2[v4] == '(':
        v3.append(v3[v4] + 1)
    else:
        v3.append(v3[v4] - 1)
v5 = min(v3)
v6 = v3[-1]
if v5 < 0:
    v2 = '(' * (-1 * v5) + v2
    v6 -= v5
if v6 >= 0:
    v2 += ')' * v6
else:
    v7 = -1 * v6
    v2 = '(' * v7 + v2
print(v2)
