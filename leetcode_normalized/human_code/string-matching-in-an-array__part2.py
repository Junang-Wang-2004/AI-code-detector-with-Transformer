class C1(object):

    def stringMatching(self, a1):
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

        def kmp(a1, a2, a3):
            if not a2:
                return 0
            if len(a1) < len(a2):
                return -1
            v1 = -1
            for v2 in range(len(a1)):
                while v1 != -1 and a2[v1 + 1] != a1[v2]:
                    v1 = a3[v1]
                if a2[v1 + 1] == a1[v2]:
                    v1 += 1
                if v1 + 1 == len(a2):
                    return v2 - v1
            return -1
        v1 = []
        for v2, v3 in enumerate(a1):
            v4 = getPrefix(v3)
            for v5, v6 in enumerate(a1):
                if v2 != v5 and kmp(v6, v3, v4) != -1:
                    v1.append(v3)
                    break
        return v1
