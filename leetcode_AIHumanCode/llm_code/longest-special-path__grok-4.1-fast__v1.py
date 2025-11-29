class Solution:
    def longestSpecialPath(self, edges, nums):
        n = len(nums)
        adj_list = [[] for _ in range(n)]
        for a, b, w in edges:
            adj_list[a].append((b, w))
            adj_list[b].append((a, w))
        last_occurrence = {}
        dist_along_path = [0]
        optimum = [float('inf'), float('inf')]
        def traverse(node, parent, depth, max_prior):
            clr = nums[node] - 1
            prior_depth = last_occurrence.get(clr, -1)
            last_occurrence[clr] = depth
            updated_max_prior = max(max_prior, prior_depth)
            path_length = dist_along_path[depth] - dist_along_path[updated_max_prior + 1]
            num_nodes = depth - updated_max_prior
            optimum[:] = min(optimum, [-path_length, num_nodes])
            for neighbor, weight in adj_list[node]:
                if neighbor == parent:
                    continue
                dist_along_path.append(dist_along_path[-1] + weight)
                traverse(neighbor, node, depth + 1, updated_max_prior)
                dist_along_path.pop()
            last_occurrence[clr] = prior_depth
        traverse(0, -1, 0, -1)
        return [-optimum[0], optimum[1]]
