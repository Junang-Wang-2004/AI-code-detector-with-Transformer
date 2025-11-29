class C1(object):

    def minArraySum(self, a1, a2):
        """
        """
        v1 = [float('inf')] * a2
        v1[0] = v2 = 0
        for v3 in a1:
            v2 += v3
            v1[v2 % a2] = v2 = min(v2, v1[v2 % a2])
        return v2
