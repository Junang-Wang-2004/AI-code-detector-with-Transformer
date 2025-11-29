# Time:  O(nlogn + qlogn)
# Space: O(nlogn)
from functools import partial


# Template:
# https://github.com/kamyu104/GoogleKickStart-2021/blob/main/Round%20H/dependent_events2.py
class TreeInfos2(object):  # Time: O(NlogN), Space: O(NlogN), N is the number of nodes
    def __init__(self, children):  # modified
        def preprocess(curr, parent):
            # depth of the node i
            D[curr] = 1 if parent == -1 else D[parent]+1
            # ancestors of the node i
            if parent != -1:
                P[curr].append(parent)
            i = 0
            while i < len(P[curr]) and i < len(P[P[curr][i]]):
                P[curr].append(P[P[curr][i]][i])
                i += 1
            # the subtree of the node i is represented by traversal index L[i]..R[i]
            C[0] += 1
            L[curr] = C[0]

        def divide(curr, parent):
            stk.append(partial(postprocess, curr))
            for i in reversed(range(len(children[curr]))):
                child = children[curr][i]
                if child == parent:
                    continue
                stk.append(partial(divide, child, curr))
            stk.append(partial(preprocess, curr, parent))

        def postprocess(curr):
            R[curr] = C[0]

        N = len(children)
        L, R, D, P, C = [0]*N, [0]*N, [0]*N, [[] for _ in range(N)], [-1]
        stk = []
        stk.append(partial(divide, 0, -1))
        while stk:
            stk.pop()()
        assert(C[0] == N-1)
        self.L, self.R, self.D, self.P = L, R, D, P

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
class Solution2(object):
    def closestNode(self, n, edges, query):
        """
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v), adj[v].append(u)
        tree_infos = TreeInfos2(adj)
        return [max((tree_infos.lca(x, y) for x, y in ((start, end), (start, node), (end, node))), key=lambda x: tree_infos.D[x]) for start, end, node in query]


