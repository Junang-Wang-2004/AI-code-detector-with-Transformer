class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, tree_a, tree_b):
        def extract_leaves(current):
            if current is None:
                return []
            if current.left is None and current.right is None:
                return [current.val]
            left_seq = extract_leaves(current.left)
            right_seq = extract_leaves(current.right)
            return left_seq + right_seq
        seq_a = extract_leaves(tree_a)
        seq_b = extract_leaves(tree_b)
        return seq_a == seq_b
