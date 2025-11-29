class C1(object):

    def calculateScore(self, a1, a2):
        """
        """
        v1 = 0
        v2 = [False] * len(a1)
        v3 = 0
        while 0 <= v3 < len(a1):
            if v2[v3]:
                break
            v2[v3] = True
            if a1[v3] == 'add':
                v1 += a2[v3]
                v3 += 1
            else:
                v3 += a2[v3]
        return v1
