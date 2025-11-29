def f1(a1, a2):
    global out
    if len(a1) == 1:
        for v1 in range(len(a2)):
            if v1 == len(a2) - 1:
                v2 += a2[v1] * 10 + int(a1[0]) + a2[v1] + int(a1[0])
            else:
                v2 += 2 * a2[v1]
        return False
    a2.append(int(a1[0]))
    if f1(a1[1:len(a1)], a2):
        return False
    a2.pop()
    if len(a2) != 0:
        a2.append(a2.pop() * 10 + int(a1[0]))
        if f1(a1[1:len(a1)], a2):
            return False
    return False
v1 = 0
v2 = []
v3 = input()
f1(v3, v2)
print(v1)
