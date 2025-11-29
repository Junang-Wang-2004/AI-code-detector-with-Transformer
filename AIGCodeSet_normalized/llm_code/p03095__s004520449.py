v1 = int(input())
v2 = input()
v3 = []
v4 = 0

def f1(a1, a2, a3):
    if a1 == v1:
        a3 += 1
        return a3
    v2 = v2[a1]
    a3 = f1(a1 + 1, a2, a3)
    if v2 not in a2:
        a2.append(v2)
        a3 = f1(a1 + 1, a2, a3)
        a2.pop()
    return a3
v5 = f1(0, v3, v4)
print(v5 - 1)
