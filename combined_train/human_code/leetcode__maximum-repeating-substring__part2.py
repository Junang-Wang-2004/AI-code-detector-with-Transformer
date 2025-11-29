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
        v1 = a2 * (len(a1) // len(a2))
        v2 = getPrefix(v1)
        v3, v4 = (0, -1)
        for v5 in range(len(a1)):
            while v4 > -1 and v1[v4 + 1] != a1[v5]:
                v4 = v2[v4]
            if v1[v4 + 1] == a1[v5]:
                v4 += 1
            v3 = max(v3, v4 + 1)
            if v4 + 1 == len(v1):
                break
        return v3 // len(a2)
