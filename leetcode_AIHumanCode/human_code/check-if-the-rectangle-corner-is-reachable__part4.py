# Time:  O(n^2)
# Space: O(n^2)
# bfs
class Solution4(object):
    def canReachCorner(self, X, Y, circles):
        """
        """
        def check(x1, y1, r1, x2, y2, r2):
            return (x1-x2)**2+(y1-y2)**2 <= (r1+r2)**2

        def bfs(src, dst):
            lookup = [False]*len(adj)
            lookup[src] = True
            q = [src]
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q = new_q
            return lookup[dst]

        adj = [[] for _ in range(len(circles)+2)]
        for u in range(len(circles)):
            x1, y1, r1 = circles[u]
            if x1-r1 <= 0 or y1+r1 >= Y:
                adj[u].append(len(circles))
                adj[len(circles)].append(u)
            if x1+r1 >= X or y1-r1 <= 0:
                adj[u].append(len(circles)+1)
                adj[len(circles)+1].append(u)
            for v in range(u):
                x2, y2, r2 = circles[v]
                if not check(x1, y1, r1, x2, y2, r2):
                    continue
                adj[u].append(v)
                adj[v].append(u)
        return not bfs(len(circles), len(circles)+1)


