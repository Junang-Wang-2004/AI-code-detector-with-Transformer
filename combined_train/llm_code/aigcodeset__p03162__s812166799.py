v1 = int(input())
v2 = [[*map(int, input().split())] for v3 in range(v1)]
v4 = 0
v5 = ''
for v3 in range(v1):
    v6, v7, v8 = v2[v3]
    if v6 > v7 and v6 > v8:
        if v5 != 'a':
            v4 += v6
            v5 = 'a'
        else:
            v9 = [v6, v7, v8]
            v9.sort()
            v10 = v2[v3 - 1].copy()
            v10.sort()
            if v2[v3 - 1][0] + v9[1] >= v10[1] + v9[-1]:
                v4 += v9[1]
                if v9[1] == v6:
                    v5 = 'a'
                elif v9[1] == v7:
                    v5 = 'b'
                else:
                    v5 = 'c'
            else:
                v4 -= v10[-1]
                v4 += v10[1] + v6
                v5 = 'a'
    elif v7 > v6 and v7 > v8:
        if v5 != 'b':
            v5 = 'b'
            v4 += v7
        else:
            v9 = [v6, v7, v8]
            v9.sort()
            v10 = v2[v3 - 1].copy()
            v10.sort()
            if v2[v3 - 1][1] + v9[1] >= v10[1] + v9[-1]:
                v4 += v9[1]
                if v9[1] == v6:
                    v5 = 'a'
                elif v9[1] == v7:
                    v5 = 'b'
                else:
                    v5 = 'c'
            else:
                v4 -= v10[-1]
                v4 += v10[1] + v7
                v5 = 'b'
    elif v8 > v6 and v8 > v7:
        if v5 != 'c':
            v4 += v8
            v5 = 'c'
        else:
            v9 = [v6, v7, v8]
            v9.sort()
            v10 = v2[v3 - 1].copy()
            v10.sort()
            if v2[v3 - 1][2] + v9[1] >= v10[1] + v9[-1]:
                v4 += v9[1]
                if v9[1] == v6:
                    v5 = 'a'
                elif v9[1] == v7:
                    v5 = 'b'
                else:
                    v5 = 'c'
            else:
                v4 -= v10[-1]
                v4 += v10[1] + v8
                v5 = 'c'
    else:
        v4 += max(v2[v3])
        v11 = max(v2[v3])
        if v11 == v6 and v5 != 'a':
            v5 = 'a'
        elif v11 == v7 and v5 != 'b':
            v5 = 'b'
        else:
            v5 = 'c'
print(v4)
