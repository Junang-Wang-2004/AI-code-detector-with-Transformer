class C1(object):

    def maxSumMinProduct(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (len(a1) + 1)
        for v3 in range(len(a1)):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4, v5 = ([-1], 0)
        for v3 in range(len(a1) + 1):
            while v4[-1] != -1 and (v3 == len(a1) or a1[v4[-1]] >= a1[v3]):
                v5 = max(v5, a1[v4.pop()] * (v2[v3 - 1 + 1] - v2[v4[-1] + 1]))
            v4.append(v3)
        return v5 % v1
