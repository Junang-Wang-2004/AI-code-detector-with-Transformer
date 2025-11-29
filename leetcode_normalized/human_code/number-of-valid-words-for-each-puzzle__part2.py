import collections
from functools import reduce

class C1(object):

    def findNumOfValidWords(self, a1, a2):
        """
        """
        v1 = 7
        v2 = collections.defaultdict(list)
        for v3 in range(len(a2)):
            v4 = []
            v5 = 1 << ord(a2[v3][0]) - ord('a')
            for v6 in range(1, v1):
                v4.append(ord(a2[v3][v6]) - ord('a'))
            for v7 in range(2 ** len(v4)):
                v8 = v5
                for v6 in range(len(v4)):
                    if v7 & 1 << v6:
                        v8 |= 1 << v4[v6]
                v2[v8].append(v3)
        v9 = [0] * len(a2)
        for v10 in a1:
            v8 = 0
            for v11 in v10:
                v8 |= 1 << ord(v11) - ord('a')
            if v8 not in v2:
                continue
            for v3 in v2[v8]:
                v9[v3] += 1
        return v9
