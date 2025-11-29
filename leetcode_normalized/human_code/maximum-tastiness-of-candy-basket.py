class C1(object):

    def maximumTastiness(self, a1, a2):
        """
        """

        def check(a1):
            v1 = v2 = 0
            for v3 in range(len(a1)):
                if v2 and a1[v3] - v2 < a1:
                    continue
                v1 += 1
                if v1 == a2:
                    break
                v2 = a1[v3]
            return v1 >= a2
        a1.sort()
        v1, v2 = (1, a1[-1] - a1[0])
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
