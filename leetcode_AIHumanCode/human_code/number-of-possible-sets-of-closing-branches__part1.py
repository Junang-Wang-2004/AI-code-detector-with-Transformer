# Time:  O(r + 2^n * n^2)
# Space: O(n^3)

# graph, bitmasks, Floyd-Warshall algorithm, backtracking
class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        """
        def check(mask, dist):
            return all(dist[i][j] <= maxDistance for i in range(n) if mask&(1<<i) for j in range(i+1, n) if mask&(1<<j))

        def floydWarshall(dist, k):
            for i in range(len(dist)):
                for j in range(i+1, len(dist[i])):
                    dist[j][i] = dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

        def backtracking(i, mask, dist):
            if i == n:
                result[0] += check(mask, dist)
                return
            for j in range(2):
                new_dist = [d[:] for d in dist]
                if j:
                    floydWarshall(new_dist, i)
                backtracking(i+1, mask|(j<<i), new_dist)
    
        dist = [[0 if u == v else float("inf") for v in range(n)] for u in range(n)]
        for u, v, w in roads:
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)
        result = [0]
        backtracking(0, 0, [d[:] for d in dist])
        return result[0]
    

