class C1:

    def strobogrammaticInRange(self, a1: str, a2: str) -> int:
        v1 = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        v2 = {}
        v3 = max(len(a1), len(a2))
        v4 = [0] * (v3 + 1)
        if v3 >= 1:
            v4[1] = 3
        if v3 >= 2:
            v4[2] = 4
        if v3 >= 3:
            v4[3] = 12
        for v5 in range(4, v3 + 1):
            v4[v5] = 5 * v4[v5 - 2]
        v6 = [0] * (v3 + 2)
        for v5 in range(1, v3 + 1):
            v6[v5] = v6[v5 - 1] + v4[v5]

        def valid_stro(a1: str) -> bool:
            v1 = len(a1)
            for v2 in range(v1 // 2 + 1):
                v3 = v1 - 1 - v2
                if a1[v3] not in v1 or a1[v2] != v1[a1[v3]]:
                    return False
            return True

        def tally_leq(a1: str, a2: bool) -> int:
            v1 = (a1, a2)
            if v1 in v2:
                return v2[v1]
            v2 = 0
            v3 = len(a1)
            if not a2:
                v2 = v6[v3 - 1]
            if v3 == 1:
                for v4 in '018':
                    if a1 >= v4:
                        v2 += 1
            else:
                for v5, v6 in v1.items():
                    if not a2 and v5 == '0':
                        continue
                    if a1[0] > v5:
                        v7 = v3 - 2
                        if v7 == 0:
                            v2 += 1
                        else:
                            v2 += tally_leq('9' * v7, True)
                    elif a1[0] == v5:
                        if v3 == 2:
                            if a1[-1] >= v6:
                                v2 += 1
                        else:
                            v8 = a1[1:-1]
                            v9 = v3 - 2
                            if a1[-1] >= v6:
                                v2 += tally_leq(v8, True)
                            elif v8 != '0' * v9:
                                v2 += tally_leq(v8, True) - (1 if valid_stro(v8) else 0)
            v2[v1] = v2
            return v2
        v7 = tally_leq(a2, False)
        v8 = tally_leq(a1, False)
        return v7 - v8 + (1 if valid_stro(a1) else 0)
