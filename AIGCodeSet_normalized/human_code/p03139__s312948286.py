v1, v2, v3 = map(int, input().split())
if v2 + v3 <= v1:
    print(str(min(v2, v3)) + ' 0')
else:
    print(str(min(v2, v3)) + ' ' + str(abs(v1 - (2 * v1 - v2 - v3))))
