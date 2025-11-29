class Solution:
    def sumOfDistancesInTree(self, n, edge_list):
        adj = [[] for _ in range(n)]
        for a, b in edge_list:
            adj[a].append(b)
            adj[b].append(a)
        sub_sz = [0] * n
        dist_sub = [0] * n
        def build_tree(curr, prev):
            sub_sz[curr] = 1
            dist_sub[curr] = 0
            for next_node in adj[curr]:
                if next_node != prev:
                    build_tree(next_node, curr)
                    sub_sz[curr] += sub_sz[next_node]
                    dist_sub[curr] += dist_sub[next_node] + sub_sz[next_node]
        build_tree(0, -1)
        ans = [0] * n
        ans[0] = dist_sub[0]
        def adjust(curr, prev):
            for next_node in adj[curr]:
                if next_node != prev:
                    ans[next_node] = ans[curr] + (n - 2 * sub_sz[next_node])
                    adjust(next_node, curr)
        adjust(0, -1)
        return ans
