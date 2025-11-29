def f1():
    import sys
    input = sys.stdin.readline
    v1, v2, v3, v4 = map(int, input().split())
    if v1 > v3:
        return '{} {} {} {}'.format(v3, v4 - (v1 - v3), v1, v2 - (v1 - v3))
    elif v1 < v3:
        return '{} {} {} {}'.format(v3, v4 + (v3 - v1), v1, v2 + (v3 - v1))
    elif v2 > v4:
        return '{} {} {} {}'.format(v3 + (v2 - v4), v4, v1 + (v2 - v4), v2)
    else:
        return '{} {} {} {}'.format(v3 - (v4 - v2), v4, v1 - (v4 - v2), v2)
print(f1())
