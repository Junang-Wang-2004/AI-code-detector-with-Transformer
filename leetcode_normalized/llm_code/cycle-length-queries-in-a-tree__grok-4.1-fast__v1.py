class C1:

    def cycleLengthQueries(self, a1, a2):
        v1 = []
        for v2, v3 in a2:
            v4 = v2.bit_length() - 1
            v5 = v3.bit_length() - 1
            v6, v7 = (v4, v5)
            if v4 > v5:
                v2 >>= v4 - v5
                v8 = v5
            elif v5 > v4:
                v3 >>= v5 - v4
                v8 = v4
            else:
                v8 = v4
            v9 = v2 ^ v3
            v10 = v9.bit_length()
            v11 = v8 - v10
            v1.append(v6 + v7 - 2 * v11 + 1)
        return v1
