v1, v2, v3 = map(int, input().split())
if v2 == 0:
    print(' '.join([str(v3 + 1)] * v1))
else:
    v4 = [str(v3)] * v2
    v5 = [str(v3 + 1)] * (v1 - v2)
    print(' '.join(v4 + v5))
