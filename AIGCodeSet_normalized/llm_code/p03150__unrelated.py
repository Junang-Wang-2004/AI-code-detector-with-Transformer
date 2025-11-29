def f1(a1):
    v1 = 'keyence'
    for v2 in range(len(a1)):
        for v3 in range(v2, len(a1)):
            if a1[:v2] + a1[v3:] == v1:
                return True
    return False
v1 = input()
print('YES' if f1(v1) else 'NO')
