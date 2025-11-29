import itertools

class C1(object):

    def minDeletionSize(self, a1):
        """
        """
        v1 = 0
        for v2 in zip(*a1):
            if any((v2[i] > v2[i + 1] for v3 in range(len(v2) - 1))):
                v1 += 1
        return v1
