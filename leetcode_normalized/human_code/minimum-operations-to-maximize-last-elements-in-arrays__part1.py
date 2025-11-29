import itertools

class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = [0] * 2
        for v2, v3 in zip(a1, a2):
            if not (min(v2, v3) <= min(a1[-1], a2[-1]) and max(v2, v3) <= max(a1[-1], a2[-1])):
                return -1
            if not (v2 <= a1[-1] and v3 <= a2[-1]):
                v1[0] += 1
            if not (v2 <= a2[-1] and v3 <= a1[-1]):
                v1[1] += 1
        return min(v1)
