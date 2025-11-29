class C1(object):

    def minDeletionSize(self, a1):
        """
        """
        v1 = 0
        v2 = [False] * (len(a1) - 1)
        for v3 in range(len(a1[0])):
            v4 = v2[:]
            for v5 in range(len(a1) - 1):
                if a1[v5][v3] > a1[v5 + 1][v3] and v4[v5] == False:
                    v1 += 1
                    break
                if a1[v5][v3] < a1[v5 + 1][v3]:
                    v4[v5] = True
            else:
                v2 = v4
        return v1
