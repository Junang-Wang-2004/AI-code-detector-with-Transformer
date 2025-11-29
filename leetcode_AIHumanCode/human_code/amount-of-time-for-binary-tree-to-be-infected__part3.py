# Time:  O(n)
# Space: O(n)
# bfs
class Solution3(object):
    def amountOfTime(self, root, start):
        """
        """
        def bfs(root):
            adj = collections.defaultdict(list)
            q = [root]
            while q:
                new_q = []
                for u in q:
                    for v in (u.left, u.right):
                        if v is None:
                            continue
                        adj[u.val].append(v.val)
                        adj[v.val].append(u.val)
                        new_q.append(v)
                q = new_q
            return adj

        def bfs2(adj, start):
            result = -1
            q = [start]
            lookup = {start}
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if v in lookup:
                            continue
                        lookup.add(v)
                        new_q.append(v)
                q = new_q
                result += 1
            return result

        adj = bfs(root)
        return bfs2(adj, start)
