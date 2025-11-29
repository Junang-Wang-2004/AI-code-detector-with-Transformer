class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        output = []
        queue = [root]
        while queue:
            level_values = []
            level_count = len(queue)
            for _ in range(level_count):
                current = queue.pop(0)
                level_values.append(current.val)
                for next_node in current.children:
                    if next_node:
                        queue.append(next_node)
            output.append(level_values)
        return output
