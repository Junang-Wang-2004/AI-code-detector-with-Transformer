class C1(object):

    def numOfSubarrays(self, a1, a2, a3):
        """
        """
        v1 = [0]
        for v2 in a1:
            v1.append(v1[-1] + v2)
        v3 = 0
        for v4 in range(len(v1) - a2):
            if v1[v4 + a2] - v1[v4] >= a3 * a2:
                v3 += 1
        return v3
