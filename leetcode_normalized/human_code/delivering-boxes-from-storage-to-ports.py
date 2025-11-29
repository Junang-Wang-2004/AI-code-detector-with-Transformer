class C1(object):

    def boxDelivering(self, a1, a2, a3, a4):
        """
        """
        v1 = [0] * (len(a1) + 1)
        v2, v3, v4 = (0, 1, 0)
        for v5 in range(len(a1)):
            if v5 == 0 or a1[v5][0] != a1[v5 - 1][0]:
                v3 += 1
            v4 += a1[v5][1]
            while v5 - v2 + 1 > a3 or v4 > a4 or (v2 + 1 < v5 + 1 and v1[v2 + 1] == v1[v2]):
                v4 -= a1[v2][1]
                if a1[v2 + 1][0] != a1[v2][0]:
                    v3 -= 1
                v2 += 1
            v1[v5 + 1] = v1[v2 - 1 + 1] + v3
        return v1[len(a1)]
