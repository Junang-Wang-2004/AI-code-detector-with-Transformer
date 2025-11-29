class C1(object):

    def minValidStrings(self, a1, a2):
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

        def KMP(a1, a2, a3):
            v1 = getPrefix(a2)
            v2 = -1
            for v3 in range(len(a1)):
                while v2 + 1 > 0 and a2[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a2[v2 + 1] == a1[v3]:
                    v2 += 1
                a3(v3, v2)
                if v2 + 1 == len(a2):
                    v2 = v1[v2]

        def update(a1, a2):
            lookup[a1] = max(lookup[a1], a2 + 1)
        v1 = [0] * len(a2)
        for v2 in a1:
            KMP(a2, v2, update)
        v3 = [0] * (len(a2) + 1)
        for v4 in range(len(a2)):
            if not v1[v4]:
                return -1
            v3[v4 + 1] = v3[v4 - v1[v4] + 1] + 1
        return v3[-1]
