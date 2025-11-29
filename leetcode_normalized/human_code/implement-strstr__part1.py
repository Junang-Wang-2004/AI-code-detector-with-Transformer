class C1(object):

    def strStr(self, a1, a2):
        """
        """
        if not a2:
            return 0
        return self.KMP(a1, a2)

    def KMP(self, a1, a2):
        v1 = self.getPrefix(a2)
        v2 = -1
        for v3 in range(len(a1)):
            while v2 > -1 and a2[v2 + 1] != a1[v3]:
                v2 = v1[v2]
            if a2[v2 + 1] == a1[v3]:
                v2 += 1
            if v2 == len(a2) - 1:
                return v3 - v2
        return -1

    def getPrefix(self, a1):
        v1 = [-1] * len(a1)
        v2 = -1
        for v3 in range(1, len(a1)):
            while v2 > -1 and a1[v2 + 1] != a1[v3]:
                v2 = v1[v2]
            if a1[v2 + 1] == a1[v3]:
                v2 += 1
            v1[v3] = v2
        return v1
