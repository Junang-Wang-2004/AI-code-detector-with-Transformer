import collections

class C1(object):

    def totalFruit(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        v2, v3 = (0, 0)
        for v4, v5 in enumerate(a1):
            v1[v5] += 1
            while len(v1) > 2:
                v1[a1[v3]] -= 1
                if v1[a1[v3]] == 0:
                    del v1[a1[v3]]
                v3 += 1
            v2 = max(v2, v4 - v3 + 1)
        return v2
