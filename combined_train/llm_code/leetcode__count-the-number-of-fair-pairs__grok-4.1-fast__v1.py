class C1(object):

    def countFairPairs(self, a1, a2, a3):
        a1.sort()
        v1 = len(a1)

        def first_ge(a1, a2):
            v1, v2 = (a1, v1 - 1)
            while v1 <= v2:
                v3 = (v1 + v2) // 2
                if a1[v3] >= a2:
                    v2 = v3 - 1
                else:
                    v1 = v3 + 1
            return v1

        def last_le(a1, a2):
            v1, v2 = (a1, v1 - 1)
            while v1 <= v2:
                v3 = (v1 + v2) // 2
                if a1[v3] <= a2:
                    v1 = v3 + 1
                else:
                    v2 = v3 - 1
            return v2
        v2 = 0
        for v3 in range(v1):
            v4 = a2 - a1[v3]
            v5 = a3 - a1[v3]
            v6 = first_ge(v3 + 1, v4)
            v7 = last_le(v3 + 1, v5)
            if v6 <= v7:
                v2 += v7 - v6 + 1
        return v2
