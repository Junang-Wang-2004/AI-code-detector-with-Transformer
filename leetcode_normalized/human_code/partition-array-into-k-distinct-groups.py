import collections

class C1(object):

    def partitionArray(self, a1, a2):
        """
        """
        if len(a1) % a2:
            return False
        v1 = len(a1) // a2
        v2 = collections.defaultdict(int)
        for v3 in a1:
            v2[v3] += 1
        return all((v3 <= v1 for v3 in v2.values()))
