class C1:

    def readBinaryWatch(self, a1):

        def count_set_bits(a1):
            v1 = 0
            while a1:
                v1 += a1 & 1
                a1 >>= 1
            return v1
        v1 = []
        for v2 in range(12):
            for v3 in range(60):
                if count_set_bits(v2) + count_set_bits(v3) == a1:
                    v1.append(f'{v2}:{v3:02d}')
        return v1
