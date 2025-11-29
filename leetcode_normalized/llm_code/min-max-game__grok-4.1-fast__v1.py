class C1:

    def minMaxGame(self, a1):

        def recurse(a1, a2):
            if a2 == 1:
                return
            v1 = a2 // 2
            for v2 in range(v1):
                v3 = a1[a1 + 2 * v2]
                v4 = a1[a1 + 2 * v2 + 1]
                a1[a1 + v2] = min(v3, v4) if v2 % 2 == 0 else max(v3, v4)
            recurse(a1, v1)
        v1 = len(a1)
        recurse(0, v1)
        return a1[0]
