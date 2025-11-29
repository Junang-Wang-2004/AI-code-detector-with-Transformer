class C1(object):

    def maximizeSweetness(self, a1, a2):
        v1 = len(a1)
        v2 = sum(a1)
        v3 = min(a1)
        v4 = v2 // (a2 + 1)

        def feasible(a1):
            v1 = 0
            v2 = 0
            while v1 < v1:
                v3 = 0
                while v1 < v1 and v3 < a1:
                    v3 += a1[v1]
                    v1 += 1
                if v3 >= a1:
                    v2 += 1
            return v2 >= a2 + 1
        while v3 <= v4:
            v5 = v3 + (v4 - v3) // 2
            if feasible(v5):
                v3 = v5 + 1
            else:
                v4 = v5 - 1
        return v4
