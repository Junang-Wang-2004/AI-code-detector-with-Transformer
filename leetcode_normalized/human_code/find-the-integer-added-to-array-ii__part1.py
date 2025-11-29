import heapq
import collections

class C1(object):

    def minimumAddedInteger(self, a1, a2):
        """
        """

        def check(a1, a2):
            return all((a2.get(k, 0) - v >= 0 for v1, v2 in a1.items()))
        v1 = max(a2)
        v2 = collections.Counter(a2)
        return next((d for v3 in [v1 - x for v4 in heapq.nlargest(3, a1)] if check(v2, collections.Counter((v4 + v3 for v4 in a1)))))
