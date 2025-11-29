import collections

class C1(object):

    def longestStrChain(self, a1):
        """
        """
        a1.sort(key=len)
        v1 = collections.defaultdict(int)
        for v2 in a1:
            for v3 in range(len(v2)):
                v1[v2] = max(v1[v2], v1[v2[:v3] + v2[v3 + 1:]] + 1)
        return max(v1.values())
