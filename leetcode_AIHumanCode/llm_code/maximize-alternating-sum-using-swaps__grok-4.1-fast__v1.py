from collections import defaultdict

class Solution(object):
    def maxAlternatingSum(self, nums, swaps):
        n = len(nums)
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
        
        for a, b in swaps:
            union(a, b)
        
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        
        total = sum(nums)
        adjustment = 0
        for positions in groups.values():
            odd_positions = sum(p % 2 for p in positions)
            values = sorted(nums[p] for p in positions)
            adjustment += sum(values[:odd_positions])
        
        return total - 2 * adjustment
