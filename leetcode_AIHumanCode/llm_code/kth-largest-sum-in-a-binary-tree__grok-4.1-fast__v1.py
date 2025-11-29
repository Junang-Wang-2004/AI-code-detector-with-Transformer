from collections import deque

class Solution:
    def kthLargestLevelSum(self, root, k):
        level_sums = []
        if not root:
            num_levels = 0
        else:
            q = deque([root])
            while q:
                curr_level_sum = 0
                sz = len(q)
                for _ in range(sz):
                    curr_node = q.popleft()
                    curr_level_sum += curr_node.val
                    if curr_node.left:
                        q.append(curr_node.left)
                    if curr_node.right:
                        q.append(curr_node.right)
                level_sums.append(curr_level_sum)
            num_levels = len(level_sums)
        if num_levels < k:
            return -1
        level_sums.sort(reverse=True)
        return level_sums[k - 1]
