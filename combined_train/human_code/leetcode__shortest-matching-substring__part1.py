class C1(object):

    def shortestMatchingSubstring(self, a1, a2):
        """
        """
        v1 = float('inf')

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
            if not a2:
                for v1 in range(len(a1) + 1):
                    yield v1
                return
            v2 = getPrefix(a2)
            v3 = -1
            for v1 in range(len(a1)):
                while v3 + 1 > 0 and a2[v3 + 1] != a1[v1]:
                    v3 = v2[v3]
                if a2[v3 + 1] == a1[v1]:
                    v3 += 1
                if v3 + 1 == len(a2):
                    yield (v1 - v3)
                    v3 = v2[v3]
        v2, v3, v4 = a2.split('*')
        v5 = len(a1)
        v6, v7, v8 = (len(v2), len(v3), len(v4))
        v9 = v1
        v10 = v11 = 0
        v12 = KMP(a1, v3)
        v13 = KMP(a1, v4)
        for v14 in KMP(a1, v2):
            while v10 != -1 and v10 < v14 + v6:
                v10 = next(v12, -1)
            if v10 == -1:
                break
            while v11 != -1 and v11 < v10 + v7:
                v11 = next(v13, -1)
            if v11 == -1:
                break
            v9 = min(v9, v11 + v8 - v14)
        return v9 if v9 != v1 else -1
