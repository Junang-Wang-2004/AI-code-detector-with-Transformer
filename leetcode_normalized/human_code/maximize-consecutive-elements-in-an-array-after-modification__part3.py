import collections

class C1(object):

    def maxSelectedElements(self, a1):
        """
        """
        a1.sort()
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2 + 1] = v1[v2] + 1
            v1[v2] = v1[v2 - 1] + 1
        return max(v1.values())
