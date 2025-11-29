class Solution:
    def pathSum(self, nums):
        if not nums:
            return 0
        node_val = {}
        for num in nums:
            lev = num // 100 - 1
            pos = (num % 100) // 10 - 1
            val = num % 10
            node_val[(lev, pos)] = val
        subtree_leaves = {}
        nodes = list(node_val)
        nodes.sort(key=lambda x: x[0], reverse=True)
        for lev, pos in nodes:
            c1 = (lev + 1, 2 * pos)
            c2 = (lev + 1, 2 * pos + 1)
            cnt = 0
            if c1 in node_val:
                cnt += subtree_leaves[c1]
            if c2 in node_val:
                cnt += subtree_leaves[c2]
            subtree_leaves[(lev, pos)] = cnt if cnt > 0 else 1
        total = 0
        for node, val in node_val.items():
            total += val * subtree_leaves[node]
        return total
