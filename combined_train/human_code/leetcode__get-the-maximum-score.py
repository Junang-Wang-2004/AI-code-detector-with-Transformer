class C1(object):

    def maxSum(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (0, 0)
        v4, v5, v6 = (0, 0, 0)
        while v2 != len(a1) or v3 != len(a2):
            if v2 != len(a1) and (v3 == len(a2) or a1[v2] < a2[v3]):
                v5 += a1[v2]
                v2 += 1
            elif v3 != len(a2) and (v2 == len(a1) or a1[v2] > a2[v3]):
                v6 += a2[v3]
                v3 += 1
            else:
                v4 = (v4 + (max(v5, v6) + a1[v2])) % v1
                v5, v6 = (0, 0)
                v2 += 1
                v3 += 1
        return (v4 + max(v5, v6)) % v1
