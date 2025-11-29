# Time:  O(r * (n + q) + nlogn + qlogn), r = max(w for _, _, w in edges)
# Space: O(r * n + nlogn)
import collections
from functools import partial


# Template:
# https://github.com/kamyu104/GoogleKickStart-2021/blob/main/Round%20H/dependent_events2.py
class TreeInfos2(object):  # Time: O(NlogN), Space: O(NlogN), N is the number of nodes
    def __init__(self, adj):  # modified
        def preprocess(u, p, w):
            # depth of the node i
            D[u] = 1 if p == -1 else D[p]+1
            # ancestors of the node i
            if p != -1:
                P[u].append(p)
            i = 0
            while i < len(P[u]) and i < len(P[P[u][i]]):
                P[u].append(P[P[u][i]][i])
                i += 1
            # the subtree of the node i is represented by traversal index L[i]..R[i]
            C[0] += 1
            L[u] = C[0]
            if w != -1:  # added
                cnt[w] += 1
            CNT[u] = cnt[:]  # added

        def divide(u, p, w):  # modified
            stk.append(partial(postprocess, u, w))  # modified
            for i in reversed(range(len(adj[u]))):
                v, nw = adj[u][i]
                if v == p:
                    continue
                stk.append(partial(divide, v, u, nw))  # modified
            stk.append(partial(preprocess, u, p, w))  # modified

        def postprocess(u, w):  # modified
            R[u] = C[0]
            if w != -1:  # added
                cnt[w] -= 1

        N = len(adj)
        L, R, D, P, C = [0]*N, [0]*N, [0]*N, [[] for _ in range(N)], [-1]
        CNT = [[0]*MAX_W for _ in range(N)]  # added
        cnt = [0]*MAX_W  # added
        stk = []
        stk.append(partial(divide, 0, -1, -1))  # modified
        while stk:
            stk.pop()()
        assert(C[0] == N-1)
        self.L, self.R, self.D, self.P = L, R, D, P
        self.CNT = CNT  # added

    # Template:
    # https://github.com/kamyu104/FacebookHackerCup-2019/blob/master/Final%20Round/little_boat_on_the_sea.py
    def is_ancestor(self, a, b):  # includes itself
        return self.L[a] <= self.L[b] <= self.R[b] <= self.R[a]

    def lca(self, a, b):
        if self.D[a] > self.D[b]:
            a, b = b, a
        if self.is_ancestor(a, b):
            return a
        for i in reversed(range(len(self.P[a]))):  # O(logN)
            if i < len(self.P[a]) and not self.is_ancestor(self.P[a][i], b):
                a = self.P[a][i]
        return self.P[a][0]


# binary lifting (online lca algorithm)
MAX_W = 26
class Solution2(object):
    def minOperationsQueries(self, n, edges, queries):
        """
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            w -= 1
            adj[u].append((v, w))
            adj[v].append((u, w))
        tree_infos = TreeInfos2(adj)
        result = [0]*len(queries)
        for i, (a, b) in enumerate(queries):
            lca = tree_infos.lca(a, b)
            result[i] = (tree_infos.D[a]+tree_infos.D[b]-2*tree_infos.D[lca])-max(tree_infos.CNT[a][w]+tree_infos.CNT[b][w]-2*tree_infos.CNT[lca][w] for w in range(MAX_W))
        return result
