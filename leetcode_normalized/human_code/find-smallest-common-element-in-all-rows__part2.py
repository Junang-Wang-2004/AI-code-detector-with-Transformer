import collections

class C1(object):

    def smallestCommonElement(self, a1):
        """
        """
        v1 = collections.Counter()
        for v2 in a1:
            for v3 in v2:
                v1[v3] += 1
                if v1[v3] == len(a1):
                    return v3
        return -1
