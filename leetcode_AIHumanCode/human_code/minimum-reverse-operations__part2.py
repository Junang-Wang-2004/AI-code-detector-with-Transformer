# Time:  O(nlogn)
# Space: O(n)
from sortedcontainers import SortedList


# bfs, sorted list
class Solution2(object):
    def minReverseOperations(self, n, p, banned, k):
        """
        """
        lookup = [False]*n
        for i in banned:
            lookup[i] = True
        d = 0
        result = [-1]*n
        result[p] = d
        sl = [SortedList(i for i in range(0, n, 2)), SortedList(i for i in range(1, n, 2))]
        sl[p%2].remove(p)
        q = [p]
        d += 1
        while q:
            new_q = []
            for p in q:
                left, right = 2*max(p-(k-1), 0)+(k-1)-p, 2*min(p+(k-1), n-1)-(k-1)-p
                for p in list(sl[left%2].irange(left, right)):
                    if not lookup[p]:
                        result[p] = d
                        new_q.append(p)
                    sl[left%2].remove(p)
            q = new_q
            d += 1
        return result
