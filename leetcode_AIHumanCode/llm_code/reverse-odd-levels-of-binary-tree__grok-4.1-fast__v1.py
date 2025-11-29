from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root):
        if not root:
            return root
        queue = deque([root])
        lvl = 0
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                level_nodes.append(queue.popleft())
            if lvl % 2 == 1:
                i = 0
                j = level_size - 1
                while i < j:
                    level_nodes[i].val, level_nodes[j].val = level_nodes[j].val, level_nodes[i].val
                    i += 1
                    j -= 1
            for node in level_nodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lvl += 1
        return root
