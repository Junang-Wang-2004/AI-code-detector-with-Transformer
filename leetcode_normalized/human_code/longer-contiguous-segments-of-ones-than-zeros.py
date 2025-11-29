class C1(object):

    def checkZeroOnes(self, a1):
        """
        """
        v1 = [0] * 2
        v2 = 0
        for v3 in range(len(a1) + 1):
            if v3 == len(a1) or (v3 >= 1 and a1[v3] != a1[v3 - 1]):
                v1[int(a1[v3 - 1])] = max(v1[int(a1[v3 - 1])], v2)
                v2 = 0
            v2 += 1
        return v1[0] < v1[1]
