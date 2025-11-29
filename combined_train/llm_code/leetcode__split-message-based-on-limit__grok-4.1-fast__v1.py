class C1(object):

    def splitMessage(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = 0
        while True:
            v2 += 1
            v5 = len(str(v2))
            if v5 > v3:
                v3 = v5
            v4 += v5
            v6 = v1 + v4 + v2 * (3 + v3)
            if v6 <= v2 * a2:
                break
            if 3 + 2 * v3 >= a2:
                return []
        if 3 + 2 * v3 >= a2:
            return []
        v7 = []
        v8 = 0
        for v9 in range(1, v2 + 1):
            v10 = len(str(v9))
            v11 = v3
            v12 = a2 - 3 - v10 - v11
            v13 = a1[v8:v8 + v12]
            v7.append(v13 + '<' + str(v9) + '/' + str(v2) + '>')
            v8 += v12
        return v7
