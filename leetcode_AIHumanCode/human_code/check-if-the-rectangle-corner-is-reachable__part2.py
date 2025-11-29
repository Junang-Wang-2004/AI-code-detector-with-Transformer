# Time:  O(n^2)
# Space: O(n)
# bfs
class Solution2(object):
    def canReachCorner(self, X, Y, circles):
        """
        """
        def check(x1, y1, r1, x2, y2, r2):
            return (x1-x2)**2+(y1-y2)**2 <= (r1+r2)**2

        def bfs():
            lookup = [False]*len(circles)
            q = []
            dst = [False]*len(circles)
            for u in range(len(circles)):
                x, y, r = circles[u]
                if x-r <= 0 or y+r >= Y:
                    lookup[u] = True
                    q.append(u)
                if x+r >= X or y-r <= 0:
                    dst[u] = True
            while q:
                new_q = []
                for u in q:
                    if dst[u]:
                        return True
                    x1, y1, r1 = circles[u]
                    for v in range(len(circles)):
                        x2, y2, r2 = circles[v]
                        if lookup[v] or not check(x1, y1, r1, x2, y2, r2):
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q = new_q
            return False

        return not bfs()


