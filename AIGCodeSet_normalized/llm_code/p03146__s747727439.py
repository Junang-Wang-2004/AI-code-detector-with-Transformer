v1 = int(input())
v2 = [-1, v1]

def f1(a1):
    if v2[a1 - 1] % 2 == 0:
        v1 = v2[a1 - 1] // 2
    else:
        v1 = 3 * v2[a1 - 1] + 1
    if v1 in v2:
        return a1
    v2.append(v1)
    return f1(a1 + 1)
print(f1(2))
