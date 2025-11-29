import collections
from functools import reduce

class C1(object):

    def longestDupSubstring(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 26

        def check(a1, a2):
            v1 = pow(v2, a2, v1)
            v2 = reduce(lambda x, y: (v2 * x + ord(y) - ord('a')) % v1, a1[:a2], 0)
            v3 = collections.defaultdict(list)
            v3[v2].append(a2 - 1)
            for v4 in range(a2, len(a1)):
                v2 = (v2 * v2 % v1 + ord(a1[v4]) - ord('a') - (ord(a1[v4 - a2]) - ord('a')) * v1 % v1) % v1
                if v2 in v3:
                    for v5 in v3[v2]:
                        if a1[v5 - a2 + 1:v5 + 1] == a1[v4 - a2 + 1:v4 + 1]:
                            return v4 - a2 + 1
                v3[v2].append(v4)
            return 0
        v3, v4 = (1, len(a1) - 1)
        while v3 <= v4:
            v5 = v3 + (v4 - v3) // 2
            if not check(a1, v5):
                v4 = v5 - 1
            else:
                v3 = v5 + 1
        v6 = check(a1, v4)
        return a1[v6:v6 + v4]
