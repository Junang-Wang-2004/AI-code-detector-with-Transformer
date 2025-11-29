v1 = int(input())

def f1(a1):
    v1 = []
    for v2 in range(1, int(a1 ** 0.5) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if v2 != a1 // v2:
                v1.append(a1 // v2)
    v1.sort()
    return v1
v2 = f1(v1)
v2 = v2[len(v2) // 2:]
if v1 // v2[0] == v2[0]:
    v2 = v2[1:]
print(sum(v2))
