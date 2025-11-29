from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root, v, d):
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        if d == 0:
            new_node = TreeNode(v)
            new_node.right = root
            return new_node
        if root is None:
            return root
        queue = deque([(root, 1)])
        while queue:
            curr_node, curr_depth = queue.popleft()
            if curr_depth == d - 1:
                prev_left = curr_node.left
                curr_node.left = TreeNode(v)
                curr_node.left.left = prev_left
                prev_right = curr_node.right
                curr_node.right = TreeNode(v)
                curr_node.right.right = prev_right
                continue
            if curr_node.left is not None:
                queue.append((curr_node.left, curr_depth + 1))
            if curr_node.right is not None:
                queue.append((curr_node.right, curr_depth + 1))
        return root
