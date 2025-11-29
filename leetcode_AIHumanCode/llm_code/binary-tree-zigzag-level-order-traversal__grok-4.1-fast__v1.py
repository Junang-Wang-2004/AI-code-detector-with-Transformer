class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        output = []
        queue = [root]
        forward = True
        while queue:
            current_level = []
            next_queue = []
            for node in queue:
                current_level.append(node.val)
                if forward:
                    if node.left:
                        next_queue.append(node.left)
                    if node.right:
                        next_queue.append(node.right)
                else:
                    if node.right:
                        next_queue.append(node.right)
                    if node.left:
                        next_queue.append(node.left)
            output.append(current_level)
            queue = next_queue
            forward = not forward
        return output
