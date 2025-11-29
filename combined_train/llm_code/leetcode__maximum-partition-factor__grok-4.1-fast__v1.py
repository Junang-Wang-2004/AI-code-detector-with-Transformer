class C1:

    def maxPartitionFactor(self, a1):
        v1 = len(a1)
        v2 = set()
        for v3 in range(v1):
            for v4 in range(v3 + 1, v1):
                v5 = abs(a1[v3][0] - a1[v4][0])
                v6 = abs(a1[v3][1] - a1[v4][1])
                v2.add(v5 + v6)
        v7 = sorted(v2)
        if not v7:
            return 0

        def is_bip(a1):
            v1 = [-1] * v1

            def color_comp(a1):
                v1 = [a1]
                v1[a1] = 0
                while v1:
                    v2 = v1.pop()
                    for v3 in range(v1):
                        if v3 == v2:
                            continue
                        v4 = abs(a1[v2][0] - a1[v3][0]) + abs(a1[v2][1] - a1[v3][1])
                        if v4 > a1:
                            continue
                        if v1[v3] == -1:
                            v1[v3] = 1 - v1[v2]
                            v1.append(v3)
                        elif v1[v3] == v1[v2]:
                            return False
                return True
            for v2 in range(v1):
                if v1[v2] == -1:
                    if not color_comp(v2):
                        return False
            return True
        v8, v9 = (0, len(v7) - 1)
        v10 = 0
        while v8 <= v9:
            v11 = v8 + (v9 - v8) // 2
            if not is_bip(v7[v11]):
                v10 = v7[v11]
                v9 = v11 - 1
            else:
                v8 = v11 + 1
        return v10
