def f1(a1):
    if a1 % 2 == 0:
        return a1 // 2
    else:
        return 3 * a1 + 1
v1 = int(input())
v2 = [v1]
v3 = 1
while True:
    v2.append(f1(v2[-1]))
    for v4 in range(len(v2) - 1):
        if v2[-1] == v2[v4]:
            v3 = len(v2)
            break
    if v3 != 1:
        break
print(v3)
