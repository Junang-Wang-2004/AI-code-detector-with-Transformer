from functools import reduce

class C1(object):

    def numberCount(self, a1, a2):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')

        def count2(a1):
            if a1 == 0:
                return 0
            v1 = v2 = 1
            for v3 in range(a1 - 1):
                v2 *= 9 - v3
                v1 += v2
            return 9 * v1

        def count(a1):
            v1 = v2 = 1
            while a1 // (v2 * 10):
                v2 *= 10
                v1 += 1
            v3 = count2(v1 - 1)
            v4 = 0
            v5 = reduce(lambda accu, i: accu * (9 - i), range(v1 - 1), 1)
            for v6 in range(v1):
                v7 = a1 // v2 % 10
                v2 //= 10
                v8 = v4 & (1 << v7) - 1 - int(v6 == 0)
                v3 += (v7 - int(v6 == 0) - popcount(v8)) * v5
                v5 //= 9 - v6
                if v4 & 1 << v7:
                    break
                v4 |= 1 << v7
            return v3
        return count(a2 + 1) - count(a1)
