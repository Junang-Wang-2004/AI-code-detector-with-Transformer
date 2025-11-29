class C1:

    def isRobotBounded(self, a1: str) -> bool:
        v1, v2 = (0, 0)
        v3 = 0
        v4 = [0, 1, 0, -1]
        v5 = [1, 0, -1, 0]
        for v6 in a1:
            if v6 == 'G':
                v1 += v4[v3]
                v2 += v5[v3]
            elif v6 == 'R':
                v3 = (v3 + 1) % 4
            else:
                v3 = (v3 + 3) % 4
        return v1 == 0 and v2 == 0 or v3 != 0
