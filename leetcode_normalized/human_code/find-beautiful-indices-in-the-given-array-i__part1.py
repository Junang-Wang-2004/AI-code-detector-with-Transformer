class C1(object):

    def beautifulIndices(self, a1, a2, a3, a4):
        """
        """

        def getPrefix(a1):
            v1 = [-1] * len(a1)
            v2 = -1
            for v3 in range(1, len(a1)):
                while v2 + 1 > 0 and a1[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a1[v2 + 1] == a1[v3]:
                    v2 += 1
                v1[v3] = v2
            return v1

        def KMP(a1, a2):
            v1 = getPrefix(a2)
            v2 = -1
            for v3 in range(len(a1)):
                while v2 + 1 > 0 and a2[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a2[v2 + 1] == a1[v3]:
                    v2 += 1
                if v2 + 1 == len(a2):
                    yield (v3 - v2)
                    v2 = v1[v2]
        v1 = []
        if not (len(a2) <= len(a1) and len(a3) <= len(a1)):
            return v1
        v2 = list(KMP(a1, a3))
        v3 = 0
        for v4 in KMP(a1, a2):
            while v3 < len(v2) and v2[v3] < v4 - a4:
                v3 += 1
            if v3 < len(v2) and v2[v3] <= v4 + a4:
                v1.append(v4)
        return v1
