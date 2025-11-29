class C1(object):

    def deleteString(self, a1):
        """
        """

        def getPrefix(a1, a2):
            v1 = [-1] * (len(a1) - a2)
            v2 = -1
            for v3 in range(1, len(a1) - a2):
                while v2 != -1 and a1[a2 + v2 + 1] != a1[a2 + v3]:
                    v2 = v1[v2]
                if a1[a2 + v2 + 1] == a1[a2 + v3]:
                    v2 += 1
                v1[v3] = v2
            return v1
        if all((x == a1[0] for v1 in a1)):
            return len(a1)
        v2 = [1] * len(a1)
        for v3 in reversed(range(len(a1) - 1)):
            v4 = getPrefix(a1, v3)
            for v5 in range(1, len(v4), 2):
                if 2 * (v4[v5] + 1) == v5 + 1:
                    v2[v3] = max(v2[v3], v2[v3 + (v4[v5] + 1)] + 1)
        return v2[0]
