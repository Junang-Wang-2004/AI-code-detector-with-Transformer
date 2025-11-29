# Time:  O(n + q * h)
# Space: O(n)
from functools import partial


# Template:
# https://github.com/kamyu104/GoogleKickStart-2021/blob/main/Round%20H/dependent_events2.py
class TreeInfos3(object):  # Time: O(N), Space: O(N), N is the number of nodes
    def __init__(self, children):  # modified
        def preprocess(curr, parent):
            # depth of the node i
            D[curr] = 1 if parent == -1 else D[parent]+1
            # ancestors of the node i
            P[curr] = parent

        def divide(curr, parent):
            for i in reversed(range(len(children[curr]))):
                child = children[curr][i]
                if child == parent:
                    continue
                stk.append(partial(divide, child, curr))
            stk.append(partial(preprocess, curr, parent))

        N = len(children)
        D, P = [0]*N, [0]*N
        stk = []
        stk.append(partial(divide, 0, -1))
        while stk:
            stk.pop()()
        self.D, self.P = D, P

    def lca(self, a, b):  # Time: O(h)
        while self.D[a] > self.D[b]:
            a = self.P[a]
        while self.D[a] < self.D[b]:
            b = self.P[b]
        while a != b:
            a, b = self.P[a], self.P[b]
        return a


# lca
class Solution3(object):
    def closestNode(self, n, edges, query):
        """
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v), adj[v].append(u)
        tree_infos = TreeInfos3(adj)
        return [max((tree_infos.lca(x, y) for x, y in ((start, end), (start, node), (end, node))), key=lambda x: tree_infos.D[x]) for start, end, node in query]


