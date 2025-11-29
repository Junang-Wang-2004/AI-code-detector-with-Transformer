import collections

class C1(object):

    def maxFreq(self, a1, a2, a3, a4):
        """
        """
        v1, v2 = (10 ** 9 + 7, 113)
        v3, v4 = (pow(v2, a3 - 1, v1), 0)
        v5 = 0
        v6, v7 = (collections.defaultdict(int), collections.defaultdict(int))
        for v8 in range(len(a1)):
            v7[a1[v8]] += 1
            if v8 - v5 + 1 > a3:
                v7[a1[v5]] -= 1
                v4 = (v4 - ord(a1[v5]) * v3) % v1
                if v7[a1[v5]] == 0:
                    v7.pop(a1[v5])
                v5 += 1
            v4 = (v4 * v2 + ord(a1[v8])) % v1
            if v8 - v5 + 1 == a3 and len(v7) <= a2:
                v6[v4] += 1
        return max(list(v6.values()) or [0])
