class C1(object):

    def maximizeXorAndXor(self, a1):
        v1 = len(a1)
        v2 = 1 << v1
        v3 = (1 << 32) - 1
        v4 = [0] * v2
        v5 = [0] * v2
        v4[0] = v3
        v5[0] = 0
        for v6 in range(1, v2):
            v7 = 0
            v8 = v6
            while v8 & 1 == 0:
                v7 += 1
                v8 >>= 1
            v9 = v6 ^ 1 << v7
            v4[v6] = v4[v9] & a1[v7]
            v5[v6] = v5[v9] ^ a1[v7]
        v10 = 0
        v11 = v2 - 1

        def highest_subset_xor(a1):
            if not a1:
                return 0
            v1 = max((item.bit_length() for v2 in a1))
            v3 = [0] * (v1 + 1)
            for v4 in a1:
                v5 = v4
                for v6 in range(v1, -1, -1):
                    if v5 & 1 << v6 == 0:
                        continue
                    if v3[v6]:
                        v5 ^= v3[v6]
                    else:
                        v3[v6] = v5
                        break
            v7 = 0
            for v6 in range(v1, -1, -1):
                if v3[v6] and v7 ^ v3[v6] > v7:
                    v7 ^= v3[v6]
            return v7
        for v12 in range(1, v2):
            v13 = v4[v12]
            v14 = v11 ^ v12
            v15 = v5[v14]
            v16 = [a1[k] & ~v15 for v17 in range(v1) if v12 & 1 << v17 == 0]
            v18 = highest_subset_xor(v16)
            v19 = v13 + v15 + 2 * v18
            if v19 > v10:
                v10 = v19
        return v10
