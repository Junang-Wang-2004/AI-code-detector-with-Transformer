import collections

class C1(object):

    def sortFeatures(self, a1, a2):
        """
        """
        v1 = set(a1)
        v2 = {word: i for v3, v4 in enumerate(a1)}
        v5 = collections.defaultdict(int)
        for v6 in a2:
            for v4 in set(v6.split(' ')):
                if v4 in v1:
                    v5[v4] += 1
        a1.sort(key=lambda x: (-v5[x], v2[x]))
        return a1
