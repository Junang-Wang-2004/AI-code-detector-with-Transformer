class C1:

    def maxPossibleScore(self, a1, a2):
        a1.sort()

        def possible(a1):
            v1 = a1[0]
            for v2 in range(1, len(a1)):
                v3 = max(v1 + a1, a1[v2])
                if v3 > a1[v2] + a2:
                    return False
                v1 = v3
            return True
        v1 = 1
        v2 = a1[-1] + a2 - a1[0]
        while v1 <= v2:
            v3 = (v1 + v2) // 2
            if possible(v3):
                v1 = v3 + 1
            else:
                v2 = v3 - 1
        return v2
