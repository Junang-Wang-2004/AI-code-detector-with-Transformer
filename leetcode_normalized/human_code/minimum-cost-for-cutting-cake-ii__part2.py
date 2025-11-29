class C1(object):

    def minimumCost(self, a1, a2, a3, a4):
        """
        """
        a3.sort(reverse=True)
        a4.sort(reverse=True)
        v1 = v2 = v3 = 0
        while v2 < len(a3) or v3 < len(a4):
            if v3 == len(a4) or (v2 < len(a3) and a3[v2] > a4[v3]):
                v1 += a3[v2] * (v3 + 1)
                v2 += 1
            else:
                v1 += a4[v3] * (v2 + 1)
                v3 += 1
        return v1
