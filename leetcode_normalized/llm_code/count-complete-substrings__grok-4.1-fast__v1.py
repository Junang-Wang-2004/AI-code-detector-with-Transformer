class C1(object):

    def countCompleteSubstrings(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        while v3 < v1:
            v4 = v3
            while v3 < v1 - 1 and abs(ord(a1[v3 + 1]) - ord(a1[v3])) <= 2:
                v3 += 1
            v5 = v3
            v6 = v5 - v4 + 1
            for v7 in range(1, 27):
                v8 = v7 * a2
                if v8 > v6:
                    break
                v9 = [0] * 26
                v10 = 0
                v11 = v4
                for v12 in range(v4, v5 + 1):
                    v13 = ord(a1[v12]) - ord('a')
                    v9[v13] += 1
                    if v9[v13] == a2:
                        v10 += 1
                    elif v9[v13] == a2 + 1:
                        v10 -= 1
                    while v12 - v11 + 1 > v8:
                        v14 = ord(a1[v11]) - ord('a')
                        if v9[v14] == a2:
                            v10 -= 1
                        elif v9[v14] == a2 + 1:
                            v10 += 1
                        v9[v14] -= 1
                        v11 += 1
                    if v12 - v11 + 1 == v8 and v10 == v7:
                        v2 += 1
            v3 += 1
        return v2
