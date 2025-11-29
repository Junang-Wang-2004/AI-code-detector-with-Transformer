class C1(object):

    def canChoose(self, a1, a2):
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
            for v3 in range(a3, len(a1)):
                while v2 + 1 > 0 and a2[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a2[v2 + 1] == a1[v3]:
                    v2 += 1
                if v2 + 1 == len(a2):
                    return v3 - v2
            return -1
        v1 = 0
        for v2 in a1:
            v1 = KMP(a2, v2, v1)
            if v1 == -1:
                return False
            v1 += len(v2)
        return True
