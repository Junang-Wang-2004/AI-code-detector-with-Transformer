class C1(object):

    def numOfStrings(self, a1, a2):
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

        def kmp(a1, a2):
            if not a2:
                return 0
            v1 = getPrefix(a2)
            if len(a1) < len(a2):
                return -1
            v2 = -1
            for v3 in range(len(a1)):
                while v2 != -1 and a2[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a2[v2 + 1] == a1[v3]:
                    v2 += 1
                if v2 + 1 == len(a2):
                    return v3 - v2
            return -1
        return sum((kmp(a2, pattern) != -1 for v1 in a1))
