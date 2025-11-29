class C1:

    def maximumStrongPairXor(self, a1):
        a1.sort()
        if not a1:
            return 0
        v1 = a1[-1].bit_length()
        v2 = 3200010
        v3 = [[-1] * 2 for v4 in range(v2)]
        v5 = [0] * v2
        v6 = 1

        def alloc():
            nonlocal node_id
            v1 = v6
            v2 += 1
            return v1

        def insert(a1, a2):
            nonlocal node_id
            v1 = 0
            for v2 in range(v1 - 1, -1, -1):
                v3 = a1 >> v2 & 1
                if v3[v1][v3] == -1:
                    v3[v1][v3] = alloc()
                v1 = v3[v1][v3]
                v5[v1] += a2

        def find_max(a1):
            v1 = 0
            v2 = 0
            for v3 in range(v1 - 1, -1, -1):
                v4 = a1 >> v3 & 1
                v5 = 1 - v4
                v6 = v3[v1][v5]
                if v6 != -1 and v5[v6] > 0:
                    v2 |= 1 << v3
                    v1 = v6
                else:
                    v6 = v3[v1][v4]
                    if v6 == -1:
                        break
                    v1 = v6
            return v2
        v7 = 0
        v8 = 0
        for v9 in range(len(a1)):
            insert(a1[v9], 1)
            while v7 <= v9 and a1[v9] > 2 * a1[v7]:
                insert(a1[v7], -1)
                v7 += 1
            v8 = max(v8, find_max(a1[v9]))
        return v8
