class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root):
        self.count = 0
        
        def traverse(curr):
            if not curr:
                return 0, 0
            l_sum, l_cnt = traverse(curr.left)
            r_sum, r_cnt = traverse(curr.right)
            total_sum = l_sum + r_sum + curr.val
            total_cnt = l_cnt + r_cnt + 1
            if total_sum // total_cnt == curr.val:
                self.count += 1
            return total_sum, total_cnt
        
        traverse(root)
        return self.count
