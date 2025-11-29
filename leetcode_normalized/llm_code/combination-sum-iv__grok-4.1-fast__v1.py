class C1:

    def combinationSum4(self, a1, a2):
        v1 = {}

        def ways_to_make(a1):
            if a1 == 0:
                return 1
            if a1 in v1:
                return v1[a1]
            v1 = 0
            for v2 in a1:
                if v2 <= a1:
                    v1 += ways_to_make(a1 - v2)
            v1[a1] = v1
            return v1
        return ways_to_make(a2)
