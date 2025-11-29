class C1(object):

    def calculateScore(self, a1):
        """
        """
        v1 = 0
        v2 = [[] for v3 in range(26)]
        for v4, v5 in enumerate(a1):
            v5 = ord(v5) - ord('a')
            if v2[25 - v5]:
                v1 += v4 - v2[25 - v5].pop()
            else:
                v2[v5].append(v4)
        return v1
