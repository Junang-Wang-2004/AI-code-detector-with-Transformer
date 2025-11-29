class C1(object):

    def minimumTime(self, a1, a2):
        """
        """

        def check(a1):
            v1 = 0
            for v2 in a1:
                if v2 - a2[v1] > a1:
                    return False
                elif v2 - a2[v1] > 0:
                    v3 = v2 - a2[v1]
                    v4 = max(a1 - 2 * v3, (a1 - v3) // 2)
                else:
                    v4 = a1
                while v1 < len(a2) and a2[v1] <= v2 + v4:
                    v1 += 1
                if v1 == len(a2):
                    return True
            return False
        a1.sort()
        a2.sort()
        v1, v2 = (0, 2 * (max(a2[-1], a1[-1]) - min(a2[0], a1[0])))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
