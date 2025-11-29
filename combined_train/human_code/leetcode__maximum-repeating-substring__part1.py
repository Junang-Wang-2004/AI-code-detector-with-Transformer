class C1(object):

    def maxRepeating(self, a1, a2):
        """
        """

        def getPrefix(a1):
            v1 = [-1] * len(a1)
            v2 = -1
            for v3 in range(1, len(a1)):
                while v2 > -1 and a1[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a1[v2 + 1] == a1[v3]:
                    v2 += 1
                v1[v3] = v2
            return v1
        if len(a1) < len(a2):
            return 0
        v1 = getPrefix(a2)
        v2, v3, v4, v5 = (0, 0, -1, -1)
        for v6 in range(len(a1)):
            while v4 > -1 and a2[v4 + 1] != a1[v6]:
                v4 = v1[v4]
            if a2[v4 + 1] == a1[v6]:
                v4 += 1
            if v4 + 1 == len(a2):
                v3 = v3 + 1 if v6 - v5 == len(a2) else 1
                v2 = max(v2, v3)
                v4, v5 = (-1, v6)
        return v2
