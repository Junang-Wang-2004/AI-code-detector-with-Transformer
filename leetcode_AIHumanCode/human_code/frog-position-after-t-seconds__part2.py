# Time:  O(n)
# Space: O(n)
# dfs solution with stack with better precision
class Solution2(object):
    def frogPosition(self, n, edges, t, target):
        """
        """                
        G = collections.defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        stk = [(t, 1, 0, 1)]
        while stk:
            t, node, parent, choices = stk.pop()
            if not t or not (len(G[node])-(parent != 0)):
                if node == target:
                    return 1.0/choices
                continue
            for child in G[node]:
                if child == parent:
                    continue
                stk.append((t-1, child, node,
                            choices*(len(G[node])-(parent != 0))))
        return 0.0


