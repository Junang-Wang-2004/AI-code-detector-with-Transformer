class C1(object):

    def pourWater(self, a1, a2, a3):
        """
        """
        for v1 in range(a2):
            v2 = a3
            for v3 in (-1, 1):
                v4 = a3
                while 0 <= v4 + v3 < len(a1) and a1[v4 + v3] <= a1[v4]:
                    if a1[v4 + v3] < a1[v4]:
                        v2 = v4 + v3
                    v4 += v3
                if v2 != a3:
                    break
            a1[v2] += 1
        return a1
