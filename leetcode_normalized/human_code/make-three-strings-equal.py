import itertools

class C1(object):

    def findMinimumOperations(self, a1, a2, a3):
        """
        """
        for v1, (v2, v3, v4) in enumerate(zip(a1, a2, a3)):
            if not v2 == v3 == v4:
                break
        else:
            v1 += 1
        return len(a1) + len(a2) + len(a3) - 3 * v1 if v1 else -1
