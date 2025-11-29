class C1(object):

    def repeatedSubstringPattern(self, a1):
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
        v1 = getPrefix(a1)
        return v1[-1] != -1 and (v1[-1] + 1) % (len(a1) - v1[-1] - 1) == 0

    def repeatedSubstringPattern2(self, a1):
        """
        """
        if not a1:
            return False
        v1 = (a1 + a1)[1:-1]
        return v1.find(a1) != -1
