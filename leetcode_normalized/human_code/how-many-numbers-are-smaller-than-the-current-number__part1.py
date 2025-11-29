import collections

class C1(object):

    def smallerNumbersThanCurrent(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        for v2 in range(max(a1) + 1):
            v1[v2] += v1[v2 - 1]
        return [v1[v2 - 1] for v2 in a1]
