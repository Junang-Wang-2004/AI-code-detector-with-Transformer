class Solution:
    def tripletCount(self, a, b, c):
        def bit_parity(n):
            n ^= n >> 32
            n ^= n >> 16
            n ^= n >> 8
            n ^= n >> 4
            n ^= n >> 2
            n ^= n >> 1
            return n & 1

        oa = sum(bit_parity(x) for x in a)
        ea = len(a) - oa
        ob = sum(bit_parity(x) for x in b)
        eb = len(b) - ob
        oc = sum(bit_parity(x) for x in c)
        ec = len(c) - oc

        total = len(a) * len(b) * len(c)
        odd_total = oa * eb * ec + ea * ob * ec + ea * eb * oc + oa * ob * oc
        return total - odd_total
