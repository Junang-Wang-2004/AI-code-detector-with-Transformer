from functools import reduce

class C1(object):

    def minimumSubarrayLength(self, a1, a2):
        """
        """

        def update(a1, a2, a3):
            for v1 in range(len(cnt)):
                if a1 < 1 << v1:
                    break
                if not a1 & 1 << v1:
                    continue
                if cnt[v1] == 0:
                    a3 ^= 1 << v1
                cnt[v1] += a2
                if cnt[v1] == 0:
                    a3 ^= 1 << v1
            return a3
        v1 = reduce(lambda x, y: x | y, a1)
        if v1 < a2:
            return -1
        v2 = [0] * v1.bit_length()
        v3 = len(a1)
        v4 = v5 = 0
        for v6 in range(len(a1)):
            v5 = update(a1[v6], +1, v5)
            while v4 <= v6 and v5 >= a2:
                v3 = min(v3, v6 - v4 + 1)
                v5 = update(a1[v4], -1, v5)
                v4 += 1
        return v3
