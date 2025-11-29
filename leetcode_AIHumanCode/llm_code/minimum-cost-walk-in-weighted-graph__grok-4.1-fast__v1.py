class Solution(object):
    def minimumCost(self, n, edges, query):
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]
            while x != root:
                next_x = parent[x]
                parent[x] = root
                x = next_x
            return root

        def unite(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pa] > rank[pb]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        for u, v, _ in edges:
            unite(u, v)

        component_and = [-1] * n
        for u, v, weight in edges:
            root_u = find(u)
            component_and[root_u] &= weight

        answer = []
        for start, end in query:
            root_start = find(start)
            root_end = find(end)
            if root_start != root_end:
                answer.append(-1)
            elif start == end:
                answer.append(0)
            else:
                answer.append(component_and[root_start])
        return answer
