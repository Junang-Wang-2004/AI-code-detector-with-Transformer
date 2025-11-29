# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def smallestFromLeaf(self, root):
        def find_min_path(curr_node):
            letter = chr(ord('a') + curr_node.val)
            if curr_node.left is None and curr_node.right is None:
                return letter
            possibilities = []
            if curr_node.left:
                possibilities.append(find_min_path(curr_node.left) + letter)
            if curr_node.right:
                possibilities.append(find_min_path(curr_node.right) + letter)
            return min(possibilities)

        return find_min_path(root)
