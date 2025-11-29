# Time:  O(o * l + k^3 + n * c * l), o = len(original), l = max(len(x) for x in original), k = len(lookups), c = len({len(x) for x in original})
# Space: O(o * l + k^2 + c + l)
import collections
import itertools


# hash table, Floyd-Warshall algorithm, dp
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
        
        lookups = collections.defaultdict(dict)
        for x in itertools.chain(original, changed):
            l = len(x)
            lookup = lookups[l]
            if x not in lookup:
                lookup[x] = len(lookup)
        dists = {l:[[0 if u == v else INF for v in range(len(lookup))] for u in range(len(lookup))] for l, lookup in lookups.items()}
        for i in range(len(original)):
            l = len(original[i])
            lookup, dist = lookups[l], dists[l]
            u, v = lookup[original[i]], lookup[changed[i]]
            dist[u][v] = min(dist[u][v], cost[i])
        for dist in dists.values():
            floydWarshall(dist)
        candidates = {len(x) for x in original}
        dp = [INF]*(max(len(x) for x in original)+1)
        dp[0] = 0
        for i in range(len(source)):
            if dp[i%len(dp)] == INF:
                continue
            if source[i] == target[i]:
                dp[(i+1)%len(dp)] = min(dp[(i+1)%len(dp)], dp[i%len(dp)])
            for l in candidates:
                if i+l > len(source):
                    continue
                lookup, dist = lookups[l], dists[l]
                u, v = source[i:i+l], target[i:i+l]
                if u in lookup and v in lookup:
                    dp[(i+l)%len(dp)] = min(dp[(i+l)%len(dp)], dp[i%len(dp)]+dist[lookup[u]][lookup[v]])
            dp[i%len(dp)] = INF
        return dp[len(source)%len(dp)] if dp[len(source)%len(dp)] != INF else -1


