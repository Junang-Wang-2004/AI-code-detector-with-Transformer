import itertools

class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = float('inf')

        def count(a1, a2):
            return sum((1 if y <= a1 and x <= a2 else v1 for v1, v2 in zip(a1, a2) if not (v1 <= a1 and v2 <= a2)))
        v2 = min(count(a1[-1], a2[-1]), count(a2[-1], a1[-1]))
        return v2 if v2 != v1 else -1
