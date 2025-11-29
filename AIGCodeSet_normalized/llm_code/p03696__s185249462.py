from collections import deque
v1 = int(input())
v2 = input()
v3 = 0
v4 = 0
v5 = deque()
for v6 in range(len(v2)):
    if v2[v6] == '(':
        v5.append(v2[v6])
    elif v5 and v5[-1] == '(':
        v5.pop()
    else:
        v5.append(v2[v6])
for v6 in range(len(v5)):
    if v5[v6] == '(':
        v3 += 1
    else:
        v4 += 1
v2 += ')' * v3
v2 = '(' * v4 + v2
print(v2)
