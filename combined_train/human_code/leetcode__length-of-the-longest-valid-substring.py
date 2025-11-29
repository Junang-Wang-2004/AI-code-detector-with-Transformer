import collections

class C1(object):

    def longestValidSubstring(self, a1, a2):
        """
        """
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        for v3 in a2:
            reduce(dict.__getitem__, v3, v2)['_end']
        v4 = 0
        v5 = len(a1) - 1
        for v6 in reversed(range(len(a1))):
            v7 = v2
            for v8 in range(v6, v5 + 1):
                if a1[v8] not in v7:
                    break
                v7 = v7[a1[v8]]
                if '_end' in v7:
                    v5 = v8 - 1
                    break
            v4 = max(v4, v5 - v6 + 1)
        return v4
