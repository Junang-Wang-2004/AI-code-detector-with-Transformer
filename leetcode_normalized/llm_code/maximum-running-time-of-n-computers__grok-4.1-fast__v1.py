class C1:

    def maxRunTime(self, a1, a2):

        def possible(a1):
            v1 = 0
            v2 = a1 * a1
            for v3 in a2:
                v1 += min(v3, a1)
                if v1 >= v2:
                    return True
            return v1 >= v2
        v1 = 0
        v2 = sum(a2) // a1 + 1 if a1 > 0 else 0
        while v1 < v2:
            v3 = (v1 + v2 + 1) // 2
            if possible(v3):
                v1 = v3
            else:
                v2 = v3 - 1
        return v1
