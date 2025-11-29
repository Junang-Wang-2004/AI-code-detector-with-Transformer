class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        def collect_paths(node, target):
            if not node:
                return []
            if not node.left and not node.right:
                return [[node.val]] if node.val == target else []
            left_subs = collect_paths(node.left, target - node.val)
            right_subs = collect_paths(node.right, target - node.val)
            all_subs = left_subs + right_subs
            return [[node.val] + path for path in all_subs]
        return collect_paths(root, sum)
