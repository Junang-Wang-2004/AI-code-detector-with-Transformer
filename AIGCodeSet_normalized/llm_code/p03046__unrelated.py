def f1(a1, a2):
    if a2 >> a1 == 1:
        return [-1]
    v1 = []
    for v2 in range(2 ** a1):
        v1.append(v2)
        v1.append(v2 ^ a2)
    return v1
v1 = int(input())
v2 = int(input())
v3 = f1(v1, v2)
if v3 == [-1]:
    print('No solution')
else:
    for v4 in range(len(v3)):
        print(v3[v4], end=' ')
