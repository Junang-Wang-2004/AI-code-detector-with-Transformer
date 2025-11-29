class C1(object):

    def shortestSuperstring(self, a1, a2):
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

        def KMP(a1, a2):
            v1 = getPrefix(a2)
            v2 = -1
            for v3 in range(len(a1)):
                while v2 + 1 > 0 and a2[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a2[v2 + 1] == a1[v3]:
                    v2 += 1
                if v2 + 1 == len(a2):
                    break
            return a1 + a2[v2 + 1:]
        v1 = KMP(a1, a2)
        v2 = KMP(a2, a1)
        return v1 if len(v1) < len(v2) else v2
