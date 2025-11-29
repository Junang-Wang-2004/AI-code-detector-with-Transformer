class Solution:
    def countHighestScoreNodes(self, parents):
        n = len(parents)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parents[i]].append(i)
        
        subtree_sizes = [0] * n
        
        def get_subtree_size(node):
            size = 1
            for child in tree[node]:
                size += get_subtree_size(child)
            subtree_sizes[node] = size
            return size
        
        get_subtree_size(0)
        
        highest = 0
        num_highest = 0
        
        for node in range(n):
            product = 1
            for child in tree[node]:
                product *= subtree_sizes[child]
            remaining = n - subtree_sizes[node]
            score = max(remaining, 1) * product
            if score > highest:
                highest = score
                num_highest = 1
            elif score == highest:
                num_highest += 1
        
        return num_highest
