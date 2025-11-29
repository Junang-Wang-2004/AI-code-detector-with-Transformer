class C1(object):

    def largestNumber(self, a1, a2):
        v1 = [-1] * (a2 + 1)
        v1[0] = 0
        for v2 in range(a2):
            if v1[v2] == -1:
                continue
            for v3 in range(9):
                v4 = v2 + a1[v3]
                if v4 > a2:
                    continue
                v1[v4] = max(v1[v4], v1[v2] + 1)
        if v1[a2] == -1:
            return '0'
        v5 = []
        v6 = a2
        for v7 in range(9, 0, -1):
            v8 = a1[v7 - 1]
            while v6 >= v8 and v1[v6] == v1[v6 - v8] + 1:
                v5.append(str(v7))
                v6 -= v8
        return ''.join(v5)
