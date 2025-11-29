class C1:

    def closedIsland(self, a1):
        v1, v2 = (len(a1), len(a1[0]))

        def sink(a1, a2):
            if a1 < 0 or a1 >= v1 or a2 < 0 or (a2 >= v2) or (a1[a1][a2] != 0):
                return False
            a1[a1][a2] = 1
            sink(a1 - 1, a2)
            sink(a1 + 1, a2)
            sink(a1, a2 - 1)
            sink(a1, a2 + 1)
            return True
        for v3 in range(v2):
            sink(0, v3)
            sink(v1 - 1, v3)
        for v4 in range(1, v1):
            sink(v4, 0)
            sink(v4, v2 - 1)
        v5 = 0
        for v6 in range(1, v1 - 1):
            for v7 in range(1, v2 - 1):
                if sink(v6, v7):
                    v5 += 1
        return v5
