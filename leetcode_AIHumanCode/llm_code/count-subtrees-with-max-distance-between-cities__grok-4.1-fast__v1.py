import collections

class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):
        adj = [[] for _ in range(n)]
        for a, b in edges:
            a -= 1
            b -= 1
            adj[a].append(b)
            adj[b].append(a)
        answer = [0] * (n - 1)
        for state in range(1, 1 << n):
            diam = self.compute_diameter(adj, state)
            if diam > 0:
                answer[diam - 1] += 1
        return answer

    def compute_diameter(self, adj, state):
        length = len(adj)
        source = 0
        while source < length and (state & (1 << source)) == 0:
            source += 1
        dists = [-1] * length
        dists[source] = 0
        q = collections.deque([source])
        visited = 1 << source
        extremum = source
        max_dist = 0
        while q:
            node = q.popleft()
            for neigh in adj[node]:
                if (state & (1 << neigh)) and dists[neigh] == -1:
                    dists[neigh] = dists[node] + 1
                    visited |= 1 << neigh
                    q.append(neigh)
                    if dists[neigh] > max_dist:
                        max_dist = dists[neigh]
                        extremum = neigh
        if visited != state:
            return 0
        dists = [-1] * length
        dists[extremum] = 0
        q = collections.deque([extremum])
        diameter = 0
        while q:
            node = q.popleft()
            diameter = max(diameter, dists[node])
            for neigh in adj[node]:
                if (state & (1 << neigh)) and dists[neigh] == -1:
                    dists[neigh] = dists[node] + 1
                    q.append(neigh)
        return diameter
