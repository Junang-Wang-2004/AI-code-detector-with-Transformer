import collections

class C1(object):

    def maxFrequencyScore(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = {}

        def powmod(a1, a2):
            if (a1, a2) not in v2:
                v2[a1, a2] = v2[a1, a2 - 1] * a1 % v1 if a2 >= 2 else a1 % v1
            return v2[a1, a2]
        v3 = v4 = 0
        v5 = collections.Counter()
        for v6 in range(len(a1)):
            if v6 >= a2:
                v4 = (v4 - powmod(a1[v6 - a2], v5[a1[v6 - a2]])) % v1
                v5[a1[v6 - a2]] -= 1
                if v5[a1[v6 - a2]]:
                    v4 = (v4 + powmod(a1[v6 - a2], v5[a1[v6 - a2]])) % v1
            if v5[a1[v6]]:
                v4 = (v4 - powmod(a1[v6], v5[a1[v6]])) % v1
            v5[a1[v6]] += 1
            v4 = (v4 + powmod(a1[v6], v5[a1[v6]])) % v1
            if v6 >= a2 - 1:
                v3 = max(v3, v4)
        return v3
