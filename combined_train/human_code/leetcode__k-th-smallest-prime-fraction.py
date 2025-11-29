class C1(object):

    def kthSmallestPrimeFraction(self, a1, a2):
        """
        """

        def check(a1, a2, a3, a4):
            v1 = [0] * 2
            v2 = 0
            v3 = 0
            for v4 in range(len(a2)):
                while v3 < len(a2):
                    if v4 < v3 and a2[v4] < a2[v3] * a1:
                        if v1[0] == 0 or v1[0] * a2[v3] < v1[1] * a2[v4]:
                            v1[0] = a2[v4]
                            v1[1] = a2[v3]
                        break
                    v3 += 1
                v2 += len(a2) - v3
            if v2 == a3:
                a4[:] = v1
            return v2 >= a3
        v1 = []
        v2, v3 = (0.0, 1.0)
        while v3 - v2 > 1e-08:
            v4 = v2 + (v3 - v2) / 2.0
            if check(v4, a1, a2, v1):
                v3 = v4
            else:
                v2 = v4
            if v1:
                break
        return v1
