# Time:  O(m * 2^m)
# Space: O(2^m)
# bitmasks, bfs
class Solution2(object):
    def maxHammingDistances(self, nums, m):
        """
        """
        q = []
        dist = [-1]*(1<<m)
        for x in nums:
            if dist[x] != -1:
                continue
            dist[x] = 0
            q.append(x)
        d = 0
        while q:
            d += 1
            new_q = []
            for u in q:
                for i in range(m):
                    if dist[u^(1<<i)] != -1:
                        continue
                    dist[u^(1<<i)] = d
                    new_q.append(u^(1<<i))
            q = new_q
        return [m-dist[((1<<m)-1)^x] for x in nums]
