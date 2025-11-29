class C1:

    def shiftDistance(self, a1, a2, a3, a4):

        def build_prefix(a1):
            v1 = [0]
            for v2 in a1:
                v1.append(v1[-1] + v2)
            return v1
        v1 = build_prefix(a3)
        v2 = build_prefix(a4)
        v3 = v1[-1]
        v4 = v2[-1]

        def next_shift(a1, a2):
            if a1 <= a2:
                return v1[a2] - v1[a1]
            return v3 + v1[a2] - v1[a1]

        def prev_shift(a1, a2):
            if a1 >= a2:
                return v2[a1 + 1] - v2[a2 + 1]
            return v4 - (v2[a2 + 1] - v2[a1 + 1])
        v5 = 0
        for v6, v7 in zip(a1, a2):
            if v6 == v7:
                continue
            v8 = ord(v6) - ord('a')
            v9 = ord(v7) - ord('a')
            v5 += min(next_shift(v8, v9), prev_shift(v8, v9))
        return v5
