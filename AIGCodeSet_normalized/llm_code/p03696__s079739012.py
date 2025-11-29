v1 = int(input())
v2 = list(input())
v3 = 0
v4 = v2.index('(')
for v5 in range(v4, v1):
    if v2[v5] == '(':
        v3 += 1
    else:
        v3 -= 1
v6 = 0
v7 = v2[::-1]
v8 = v7.index(')')
for v9 in range(v8, v1):
    if v7[v9] == ')':
        v6 += 1
    else:
        v6 -= 1
v10 = ')' * max(0, v3)
v11 = '(' * max(0, v6)
v12 = ''.join(v2)
print(v11 + v12 + v10)
