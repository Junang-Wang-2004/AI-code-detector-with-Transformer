class C1(object):

    def minimumString(self, a1, a2, a3):
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

        def KMP(a1, a2):
            v1 = getPrefix(a2)
            v2 = -1
            for v3 in range(len(a1)):
                while v2 != -1 and a2[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a2[v2 + 1] == a1[v3]:
                    v2 += 1
                if v2 + 1 == len(a2):
                    return v3 - v2
            return -1

        def merge(a1, a2):
            if KMP(a2, a1) != -1:
                return a2
            v1 = getPrefix(a2 + '#' + a1)
            v2 = v1[-1] + 1
            return a1 + a2[v2:]
        v1 = [merge(a1, merge(a2, a3)), merge(a1, merge(a3, a2)), merge(a2, merge(a1, a3)), merge(a2, merge(a3, a1)), merge(a3, merge(a1, a2)), merge(a3, merge(a2, a1))]
        return min(v1, key=lambda x: (len(x), x))
