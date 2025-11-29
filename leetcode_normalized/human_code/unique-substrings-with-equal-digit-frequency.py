import collections

class C1(object):

    def equalDigitFrequency(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 27
        v3 = set()
        for v4 in range(len(a1)):
            v5 = collections.Counter()
            v6 = v7 = 0
            for v8 in range(v4, len(a1)):
                v9 = ord(a1[v8]) - ord('0') + 1
                v6 = (v6 * v2 + v9) % v1
                v5[v9] += 1
                v7 = max(v7, v5[v9])
                if len(v5) * v7 == v8 - v4 + 1:
                    v3.add(v6)
        return len(v3)
