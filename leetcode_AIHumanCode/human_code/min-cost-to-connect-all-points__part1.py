# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        """
        result, u = 0, 0  # we can start from any node as u
        dist = [float("inf")]*len(points)
        lookup = set()
        for _ in range(len(points)-1):
            x0, y0 = points[u]
            lookup.add(u)
            for v, (x, y) in enumerate(points):
                if v in lookup:
                    continue
                dist[v] = min(dist[v], abs(x-x0) + abs(y-y0))
            val, u = min((val, v) for v, val in enumerate(dist)) 
            dist[u] = float("inf")  # used
            result += val
        return result



