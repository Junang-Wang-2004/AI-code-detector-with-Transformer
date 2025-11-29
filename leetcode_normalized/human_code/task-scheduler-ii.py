import collections

class C1(object):

    def taskSchedulerII(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = 0
        for v3 in a1:
            v2 = max(v1[v3], v2 + 1)
            v1[v3] = v2 + a2 + 1
        return v2
