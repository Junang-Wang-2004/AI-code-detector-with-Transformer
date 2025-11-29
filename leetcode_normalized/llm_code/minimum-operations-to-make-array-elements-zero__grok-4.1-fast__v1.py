class C1:

    def minOperations(self, a1):

        def num_digits_base4(a1):
            if a1 < 1:
                return 0
            return (a1.bit_length() - 1) // 2 + 1

        def sum_up_to(a1):
            if a1 < 1:
                return 0
            v1 = num_digits_base4(a1)
            if v1 == 1:
                return a1
            v2 = v1 - 1
            v3 = pow(4, v2)
            v4 = (1 + (3 * v2 - 1) * v3) // 9
            v5 = 3 * v4
            v6 = v3
            v7 = a1 - v6 + 1
            v8 = v1 * v7
            return v5 + v8
        v1 = 0
        for v2 in a1:
            v3, v4 = v2
            v5 = sum_up_to(v4) - sum_up_to(v3 - 1)
            v1 += (v5 + 1) // 2
        return v1
