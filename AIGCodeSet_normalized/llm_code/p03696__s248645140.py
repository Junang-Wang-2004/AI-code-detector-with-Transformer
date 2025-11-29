from sys import stdin
v1 = int(stdin.readline().rstrip())
v2 = stdin.readline().rstrip()
v3 = ''
v4 = 0
for v5 in range(v1):
    if v2[v5] == '(':
        v3 += '('
        v4 += 1
    elif v4 > 0:
        v3 += ')'
        v4 -= 1
    else:
        v3 = '(' + v3
        v4 += 1
if v4 > 0:
    v3 += ')' * v4
print(v3)
