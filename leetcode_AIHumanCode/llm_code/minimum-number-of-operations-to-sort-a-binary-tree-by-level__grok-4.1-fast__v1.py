class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minimumOperations(self, root):
        if not root:
            return 0
        total = 0
        current_level = [root]
        while current_level:
            level_vals = []
            next_level = []
            for nd in current_level:
                level_vals.append(nd.val)
                if nd.left:
                    next_level.append(nd.left)
                if nd.right:
                    next_level.append(nd.right)
            m = len(level_vals)
            pos_map = [(level_vals[k], k) for k in range(m)]
            pos_map.sort()
            seen = [False] * m
            num_cycles = 0
            for start in range(m):
                if seen[start]:
                    continue
                num_cycles += 1
                cur = start
                while not seen[cur]:
                    seen[cur] = True
                    cur = pos_map[cur][1]
            total += m - num_cycles
            current_level = next_level
        return total
