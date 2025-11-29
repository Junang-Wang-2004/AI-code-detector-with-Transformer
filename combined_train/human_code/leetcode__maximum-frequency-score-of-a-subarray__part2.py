import collections

class C1(object):

    def maxFrequencyScore(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = v3 = 0
        v4 = collections.Counter()
        for v5 in range(len(a1)):
            if v5 >= a2:
                v3 = (v3 - pow(a1[v5 - a2], v4[a1[v5 - a2]], v1)) % v1
                v4[a1[v5 - a2]] -= 1
                if v4[a1[v5 - a2]]:
                    v3 = (v3 + pow(a1[v5 - a2], v4[a1[v5 - a2]], v1)) % v1
            if v4[a1[v5]]:
                v3 = (v3 - pow(a1[v5], v4[a1[v5]], v1)) % v1
            v4[a1[v5]] += 1
            v3 = (v3 + pow(a1[v5], v4[a1[v5]], v1)) % v1
            if v5 >= a2 - 1:
                v2 = max(v2, v3)
        return v2
