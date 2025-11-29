class C1:

    def minLength(self, a1, a2):
        v1 = len(a1)

        def possible(a1):
            if a1 == 1:
                v1 = 0
                for v2 in range(v1):
                    if int(a1[v2]) != v2 % 2:
                        v1 += 1
                return min(v1, v1 - v1) <= a2
            v3 = 0
            v4 = 1
            for v2 in range(1, v1):
                if a1[v2] == a1[v2 - 1]:
                    v4 += 1
                else:
                    v3 += v4 // (a1 + 1)
                    v4 = 1
            v3 += v4 // (a1 + 1)
            return v3 <= a2
        v2, v3 = (1, v1)
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if possible(v4):
                v3 = v4
            else:
                v2 = v4 + 1
        return v2
