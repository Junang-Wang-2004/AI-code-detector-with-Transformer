class Solution:
    def maxScore(self, edges):
        n = len(edges)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            parent, weight = edges[i]
            tree[parent].append((i, weight))
        
        def compute(node):
            subtrees = [compute(child) for child, _ in tree[node]]
            if not subtrees:
                return 0, 0
            
            child_maximums = [max(covered, uncovered) for covered, uncovered in subtrees]
            total_uncovered = sum(child_maximums)
            
            covered_max = float('-inf')
            for idx, (child, weight) in enumerate(tree[node]):
                covered_child, uncovered_child = subtrees[idx]
                child_max = child_maximums[idx]
                option = total_uncovered - child_max + uncovered_child + weight
                if option > covered_max:
                    covered_max = option
            
            return covered_max, total_uncovered
        
        root_covered, root_uncovered = compute(0)
        return max(root_covered, root_uncovered)
