# Time:  O(q + n)
# Space: O(n)

import collections


# bfs
class Solution(object):
    def numberOfNodes(self, n, queries):
        """
        """
        def bfs():
            result = 0
            q = [(1, 0)]
            while q:
                new_q = []
                for u, curr in q:
                    curr ^= cnt[u]%2
                    result += curr
                    for v in range(2*u, min(2*u+1, n)+1):
                        q.append((v, curr))
                q = new_q
            return result

        cnt = collections.Counter(queries)
        return bfs()


