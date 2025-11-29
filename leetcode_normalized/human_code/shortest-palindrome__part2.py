class C1(object):

    def shortestPalindrome(self, a1):
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
        if not a1:
            return a1
        v1 = a1 + a1[::-1]
        v2 = getPrefix(v1)
        v3 = v2[-1]
        while v3 >= len(a1):
            v3 = v2[v3]
        return a1[v3 + 1:][::-1] + a1
