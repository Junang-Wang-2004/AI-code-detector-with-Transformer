class Solution:
    def minOperations(self, queries):
        def num_digits_base4(n):
            if n < 1:
                return 0
            return ((n).bit_length() - 1) // 2 + 1

        def sum_up_to(n):
            if n < 1:
                return 0
            digs = num_digits_base4(n)
            if digs == 1:
                return n
            prev = digs - 1
            p4 = pow(4, prev)
            s = (1 + (3 * prev - 1) * p4) // 9
            complete = 3 * s
            group_begin = p4
            rem = n - group_begin + 1
            extra = digs * rem
            return complete + extra

        total = 0
        for interv in queries:
            lo, hi = interv
            sm = sum_up_to(hi) - sum_up_to(lo - 1)
            total += (sm + 1) // 2
        return total
