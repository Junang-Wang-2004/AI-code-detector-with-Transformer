class C1(object):

    def mergeArrays(self, a1, a2):
        v1 = []
        v2, v3 = (0, 0)
        v4, v5 = (len(a1), len(a2))
        while v2 < v4 or v3 < v5:
            if v3 == v5 or (v2 < v4 and a1[v2][0] < a2[v3][0]):
                v1.append(a1[v2])
                v2 += 1
            else:
                v1.append(a2[v3])
                v3 += 1
        if not v1:
            return []
        v6 = []
        v7 = list(v1[0])
        for v8 in v1[1:]:
            if v8[0] == v7[0]:
                v7[1] += v8[1]
            else:
                v6.append(v7)
                v7 = list(v8)
        v6.append(v7)
        return v6
