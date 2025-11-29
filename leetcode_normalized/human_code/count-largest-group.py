import collections

class C1(object):

    def countLargestGroup(self, a1):
        """
        """
        v1 = collections.Counter()
        for v2 in range(1, a1 + 1):
            v1[sum(map(int, str(v2)))] += 1
        v3 = max(v1.values())
        return sum((v == v3 for v4 in v1.values()))
