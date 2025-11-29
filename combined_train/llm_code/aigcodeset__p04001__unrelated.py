def f1(a1):
    v1 = len(a1)
    v2 = 0
    for v3 in range(1 << v1 - 1):
        v4 = 0
        v5 = '+'
        for v6 in range(v1):
            if v3 >> v6 & 1:
                v4 += int(a1[v6])
                v5 = '+'
            else:
                if v5 == '+':
                    v4 += int(a1[v6])
                else:
                    v4 = v4 * 10 + int(a1[v6])
                v5 = ''
        v2 += v4
    return v2
v1 = input()
print(f1(v1))
