class C1:

    def findMaximumNumber(self, a1, a2):

        def get_block_size(a1, a2, a3):
            v1 = a2
            v2 = 0
            while True:
                v3 = 1 << v2 if (v2 + 1) % a3 == 0 else 0
                if (v1 << 1) + v3 > a1:
                    return (v2, v1)
                v1 = (v1 << 1) + v3
                v2 += 1
        v1 = 0
        v2 = 0
        while a1 >= v2:
            v3, v4 = get_block_size(a1, v2, a2)
            a1 -= v4
            v1 |= 1 << v3
            if (v3 + 1) % a2 == 0:
                v2 += 1
        return v1 - 1
