class C1(object):

    def findLUSlength(self, a1):
        """
        """

        def isSubsequence(a1, a2):
            v1 = 0
            for v2 in range(len(a2)):
                if v1 >= len(a1):
                    break
                if a1[v1] == a2[v2]:
                    v1 += 1
            return v1 == len(a1)
        a1.sort(key=len, reverse=True)
        for v1 in range(len(a1)):
            v2 = True
            for v3 in range(len(a1)):
                if len(a1[v3]) < len(a1[v1]):
                    break
                if v1 != v3 and isSubsequence(a1[v1], a1[v3]):
                    v2 = False
                    break
            if v2:
                return len(a1[v1])
        return -1
