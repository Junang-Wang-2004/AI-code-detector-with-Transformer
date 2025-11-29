class C1(object):

    def elementInNums(self, a1, a2):
        v1 = len(a1)
        v2 = 2 * v1
        v3 = []
        for v4 in a2:
            v5, v6 = v4
            v7 = v5 % v2
            if v7 < v1:
                v8 = v1 - v7
                v9 = a1[v7 + v6]
            else:
                v8 = v7 - v1
                v9 = a1[v6]
            if v6 < v8:
                v3.append(v9)
            else:
                v3.append(-1)
        return v3
