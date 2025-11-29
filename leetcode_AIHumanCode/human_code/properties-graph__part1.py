# Time:  O(n^2 * m)
# Space: O(n)

# graph, flood fill, bfs
class Solution(object):
    def numberOfComponents(self, properties, k):
        """
        """
        def bfs(u):
            q = [u]
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q = new_q

        p_set = [set(p) for p in properties]
        adj = [[] for _ in range(len(properties))]
        for i in range(len(p_set)):
            for j in range(i+1, len(p_set)):
                if sum(x in p_set[j] for x in p_set[i]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)
        lookup = [False]*len(properties)
        result = 0
        for i in range(len(properties)):
            if lookup[i]:
                continue
            bfs(i)
            result += 1
        return result


