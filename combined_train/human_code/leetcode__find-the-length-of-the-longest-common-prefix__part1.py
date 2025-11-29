from functools import reduce

class C1(object):

    def longestCommonPrefix(self, a1, a2):
        """
        """
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        for v3 in a1:
            reduce(dict.__getitem__, str(v3), v2)
        v4 = 0
        for v3 in a2:
            v5 = v2
            for v6, v7 in enumerate(str(v3)):
                if v7 not in v5:
                    break
                v5 = v5[v7]
            else:
                v6 += 1
            v4 = max(v4, v6)
        return v4
