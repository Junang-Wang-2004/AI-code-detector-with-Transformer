class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        def compute_total(node):
            return node.val + compute_total(node.left) + compute_total(node.right) if node else 0
        overall_sum = compute_total(root)
        max_value = 0
        def traverse(node):
            nonlocal max_value
            if not node:
                return 0
            subtree_sum = node.val + traverse(node.left) + traverse(node.right)
            max_value = max(max_value, subtree_sum * (overall_sum - subtree_sum))
            return subtree_sum
        traverse(root)
        return max_value % MOD
