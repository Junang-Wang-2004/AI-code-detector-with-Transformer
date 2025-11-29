class C1(object):

    def maxPower(self, a1, a2, a3):
        """
        """

        def min_power():
            v1 = float('inf')
            v2 = sum((a1[i] for v3 in range(a2)))
            for v3 in range(len(a1)):
                if v3 + a2 < len(a1):
                    v2 += a1[v3 + a2]
                if v3 >= a2 + 1:
                    v2 -= a1[v3 - (a2 + 1)]
                v1 = min(v1, v2)
            return v1

        def check(a1):
            v1 = a1[:]
            v2 = sum((v1[i] for v3 in range(a2)))
            v4 = a3
            for v3 in range(len(v1)):
                if v3 + a2 < len(v1):
                    v2 += v1[v3 + a2]
                if v3 >= a2 + 1:
                    v2 -= v1[v3 - (a2 + 1)]
                if v2 >= a1:
                    continue
                v5 = a1 - v2
                if v5 > v4:
                    return False
                v4 -= v5
                v2 += v5
                if v3 + a2 < len(v1):
                    v1[v3 + a2] += v5
            return True
        v1 = min_power()
        v2, v3 = (v1, v1 + a3)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if not check(v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v3
