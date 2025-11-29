class C1:

    def canPartitionKSubsets(self, a1, a2):
        v1 = sum(a1)
        if v1 % a2 != 0:
            return False
        v2 = v1 // a2
        if max(a1) > v2:
            return False
        v3 = len(a1)
        v4 = (1 << v3) - 1
        v5 = [0] * (1 << v3)
        for v6 in range(v3):
            v7 = 1 << v6
            v8 = a1[v6] % v2
            for v9 in range(1 << v3):
                if v9 & v7 == 0:
                    v5[v9 | v7] = (v5[v9] + v8) % v2
        v10 = [False] * (1 << v3)
        v10[0] = True
        for v9 in range(1 << v3):
            if not v10[v9]:
                continue
            v11 = v5[v9]
            for v6 in range(v3):
                if v9 & 1 << v6 != 0:
                    continue
                if v11 + a1[v6] > v2:
                    continue
                v12 = v9 | 1 << v6
                v10[v12] = True
        return v10[v4]
