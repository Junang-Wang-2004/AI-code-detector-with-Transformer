from collections import deque

class Solution:
    def minimumTotalPrice(self, n, edges, price, trips):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        freq = [0] * n
        for src, dst in trips:
            if src == dst:
                freq[src] += 1
                continue
            parent = [-1] * n
            q = deque([src])
            parent[src] = -2
            found = False
            while q and not found:
                curr = q.popleft()
                for neigh in graph[curr]:
                    if parent[neigh] == -1:
                        parent[neigh] = curr
                        q.append(neigh)
                        if neigh == dst:
                            found = True
                            break
            # increment along path
            curr = dst
            while curr != src:
                freq[curr] += 1
                curr = parent[curr]
            freq[src] += 1
        
        def tree_dp(node, par):
            no_cut = price[node] * freq[node]
            cut = (price[node] // 2) * freq[node]
            for neigh in graph[node]:
                if neigh == par:
                    continue
                child_no, child_cut = tree_dp(neigh, node)
                no_cut += min(child_no, child_cut)
                cut += child_no
            return no_cut, cut
        
        root_no, root_cut = tree_dp(0, -1)
        return min(root_no, root_cut)
