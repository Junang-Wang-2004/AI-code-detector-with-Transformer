# Time:  O(o * l + k^3 + n * l), o = len(original), l = max(len(x) for x in original), k = trie.k
# Space: O(t + k^2 + l)
import itertools


# trie, Floyd-Warshall algorithm, dp
class Solution6(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        """
        INF = float("inf")
        class Trie(object):
            def __init__(self):
                self.__nodes = []
                self.__idxs = []
                self.k = 0
                self.__new_node()
            
            def __new_node(self):
                self.__nodes.append([-1]*26)
                self.__idxs.append(-1)
                return len(self.__nodes)-1

            def add(self, s):
                curr = 0
                for c in s:
                    x = ord(c)-ord('a')
                    if self.__nodes[curr][x] == -1:
                        self.__nodes[curr][x] = self.__new_node()
                    curr = self.__nodes[curr][x]
                if self.__idxs[curr] == -1:
                    self.__idxs[curr] = self.k
                    self.k += 1
                    return True, self.__idxs[curr]
                return False, self.__idxs[curr]
            
            def query(self, s):
                curr = 0
                for c in s:
                    curr = self.__nodes[curr][ord(c)-ord('a')]
                return self.__idxs[curr]
    
            def next(self, curr, c):
                return self.__nodes[curr][ord(c)-ord('a')]

            def id(self, curr):
                return self.__idxs[curr]

        def floydWarshall(dist):
            for k in dist.keys():
                for i in dist.keys():
                    if dist[i][k] == INF:
                        continue
                    for j in dist.keys():
                        if dist[k][j] == INF:
                            continue
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        
        trie = Trie()
        buckets = collections.defaultdict(list)
        for x in itertools.chain(original, changed):
            not_duplicated, i = trie.add(x)
            if not_duplicated:
                buckets[len(x)].append(i)
        dists = {l:{u:{v:0 if u == v else INF for v in lookup} for u in lookup} for l, lookup in buckets.items()}
        for i in range(len(original)):
            l = len(original[i])
            dist = dists[l]
            u, v = trie.query(original[i]), trie.query(changed[i])
            dist[u][v] = min(dist[u][v], cost[i])
        for dist in dists.values():
            floydWarshall(dist)
        dp = [INF]*(max(len(x) for x in original)+1)
        dp[0] = 0
        for i in range(len(source)):
            if dp[i%len(dp)] == INF:
                continue
            if source[i] == target[i]:
                dp[(i+1)%len(dp)] = min(dp[(i+1)%len(dp)], dp[i%len(dp)])
            u = v = 0
            for j in range(i, len(source)):
                u = trie.next(u, source[j])
                v = trie.next(v, target[j])
                if u == -1 or v == -1:
                    break
                if trie.id(u) != -1 and trie.id(v) != -1:
                    dp[(j+1)%len(dp)] = min(dp[(j+1)%len(dp)], dp[i%len(dp)]+dists[j-i+1][trie.id(u)][trie.id(v)])
            dp[i%len(dp)] = INF
        return dp[len(source)%len(dp)] if dp[len(source)%len(dp)] != INF else -1
