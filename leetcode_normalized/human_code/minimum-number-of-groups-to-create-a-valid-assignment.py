import collections

class C1(object):

    def minGroupsForValidAssignment(self, a1):
        """
        """
        v1 = float('inf')

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2

        def count(a1):
            v1 = 0
            for v2 in cnt.values():
                if v2 % a1 > v2 // a1:
                    return v1
                v1 += ceil_divide(v2, a1 + 1)
            return v1
        v2 = collections.Counter(a1)
        for v3 in reversed(range(1, min(v2.values()) + 1)):
            v4 = count(v3)
            if v4 != v1:
                return v4
        return 0
