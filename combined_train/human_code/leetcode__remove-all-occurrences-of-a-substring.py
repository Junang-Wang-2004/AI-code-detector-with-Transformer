class C1(object):

    def removeOccurrences(self, a1, a2):
        """
        """

        def getPrefix(a1):
            v1 = [-1] * len(a1)
            v2 = -1
            for v3 in range(1, len(a1)):
                while v2 != -1 and a1[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a1[v2 + 1] == a1[v3]:
                    v2 += 1
                v1[v3] = v2
            return v1
        v1 = getPrefix(a2)
        v2, v3 = ([], [])
        v4 = -1
        for v5 in a1:
            while v4 != -1 and a2[v4 + 1] != v5:
                v4 = v1[v4]
            if a2[v4 + 1] == v5:
                v4 += 1
            v2.append(v5)
            v3.append(v4)
            if v4 == len(a2) - 1:
                v2[len(v2) - len(a2):] = []
                v3[len(v3) - len(a2):] = []
                v4 = v3[-1] if v3 else -1
        return ''.join(v2)
