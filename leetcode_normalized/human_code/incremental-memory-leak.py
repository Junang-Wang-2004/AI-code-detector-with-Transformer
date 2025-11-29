class C1(object):

    def memLeak(self, a1, a2):
        """
        """

        def s(a1, a2, a3):
            return (2 * a1 + (a3 - 1) * a2) * a3 // 2

        def f(a1, a2, a3):
            v1 = int((-(2 * a1 - a2) + ((2 * a1 - a2) ** 2 + 8 * a2 * a3) ** 0.5) / (2 * a2))
            if s(a1, a2, v1) > a3:
                v1 -= 1
            return v1
        v1 = False
        if a1 < a2:
            a1, a2 = (a2, a1)
            v1 = True
        v4 = f(1, 1, a1 - a2)
        a1 -= s(1, 1, v4)
        if a1 == a2:
            v1 = False
        v5 = f(v4 + 1, 2, a1)
        v6 = f(v4 + 2, 2, a2)
        a1 -= s(v4 + 1, 2, v5)
        a2 -= s(v4 + 2, 2, v6)
        if v1:
            a1, a2 = (a2, a1)
        return [v4 + v5 + v6 + 1, a1, a2]
