class C1(object):

    def rotateString(self, a1, a2):
        """
        """

        def strStr(a1, a2):

            def KMP(a1, a2):
                v1 = getPrefix(a2)
                v2 = -1
                for v3 in range(len(a1)):
                    while v2 > -1 and a2[v2 + 1] != a1[v3]:
                        v2 = v1[v2]
                    if a2[v2 + 1] == a1[v3]:
                        v2 += 1
                    if v2 == len(a2) - 1:
                        return v3 - v2
                return -1

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
            if not a2:
                return 0
            return KMP(a1, a2)
        if len(a1) != len(a2):
            return False
        return strStr(a1 * 2, a2) != -1
