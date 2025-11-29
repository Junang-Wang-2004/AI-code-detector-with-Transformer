class C1(object):

    def numberOfPairs(self, a1):
        """
        """
        a1.sort(key=lambda x: (x[0], -x[1]))
        v1 = 0
        for v2 in range(len(a1)):
            v3 = float('-inf')
            for v4 in range(v2 + 1, len(a1)):
                if a1[v2][1] < a1[v4][1]:
                    continue
                if a1[v4][1] > v3:
                    v3 = a1[v4][1]
                    v1 += 1
        return v1
