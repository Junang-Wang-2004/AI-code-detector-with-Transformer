import collections

class C1(object):

    def minimumOperationsToMakeKPeriodic(self, a1, a2):
        """
        """
        v1 = collections.Counter((a1[i:i + a2] for v2 in range(0, len(a1), a2)))
        return len(a1) // a2 - max(v1.values())
