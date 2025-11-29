class C1(object):

    def findPrefixScore(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v1 = max(v1, a1[v2])
            a1[v2] += (a1[v2 - 1] if v2 - 1 >= 0 else 0) + v1
        return a1
