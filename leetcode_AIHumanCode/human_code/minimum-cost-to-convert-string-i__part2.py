# Time:  O(o + 26^3 + n)
# Space: O(o + 26^2)
# Floyd-Warshall algorithm 
class Solution2(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        """
        INF = float("inf")
        def floydWarshall(dist):
            for k in range(len(dist)):
                for i in range(len(dist)):
                    if dist[i][k] == INF:
                        continue
                    for j in range(len(dist[i])):
                        if dist[k][j] == INF:
                            continue
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

        dist = [[0 if u == v else INF for v in range(26)] for u in range(26)]
        for i in range(len(original)):
            u, v = ord(original[i])-ord('a'), ord(changed[i])-ord('a')
            dist[u][v] = min(dist[u][v], cost[i])
        floydWarshall(dist)
        result = sum(dist[ord(source[i])-ord('a')][ord(target[i])-ord('a')] for i in range(len(source)))
        return result if result != INF else -1
