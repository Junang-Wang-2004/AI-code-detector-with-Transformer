v1 = int(input())
v2 = ((8 * v1 + 1) ** 0.5 + 1) / 2

def f1(a1):
    if a1 == 3:
        return [[1, 2], [1, 3], [2, 3]]
    else:
        v1 = f1(a1 - 1)
        v2 = [_ for v3 in range(1 + (a1 - 2) * (a1 - 1) // 2, 1 + a1 * (a1 - 1) // 2)]
        return [v1[v3] + [v2[v3]] for v3 in range(len(v2))] + [v2]
if v2.is_integer() and v2 > 1:
    v2 = int(v2)
    print('Yes')
    print(v2)
    v3 = f1(v2)
    for v4 in range(len(v3)):
        print(len(v3[v4]), ''.join(map(str, v3[v4])))
else:
    print('No')
