import itertools

class C1(object):

    def largestVariance(self, a1):
        """
        """

        def modified_kadane(a1, a2, a3):
            v1 = v2 = 0
            v3 = [0] * 2
            v4 = [a1.count(a2), a1.count(a3)]
            for v5 in a1:
                if v5 not in (a2, a3):
                    continue
                v3[v5 != a2] = 1
                v4[v5 != a2] -= 1
                v2 += 1 if v5 == a2 else -1
                if v2 < 0 and v4[0] and v4[1]:
                    v2 = v3[0] = v3[1] = 0
                if v3[0] and v3[1]:
                    v1 = max(v1, v2)
            return v1
        v1 = set(a1)
        return max((modified_kadane(a1, x, y) for v2, v3 in itertools.permutations(v1, 2))) if len(v1) >= 2 else 0
