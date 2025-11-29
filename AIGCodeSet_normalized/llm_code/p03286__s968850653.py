def f1():
    v1 = int(input().rstrip())
    v2 = 1
    v3 = []
    while v1 != 0:
        v4 = v1 % (v2 * 2)
        if v4 == 0:
            v3.append('0')
        else:
            v3.append('1')
            v1 -= v2
        v2 *= -2
    return ''.join(reversed(v3))
print(f1())
