class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        output = []
        bfs_queue = [root]
        pos = 0
        while pos < len(bfs_queue):
            batch_size = len(bfs_queue) - pos
            this_batch = []
            for _ in range(batch_size):
                curr_node = bfs_queue[pos]
                this_batch.append(curr_node.val)
                if curr_node.left:
                    bfs_queue.append(curr_node.left)
                if curr_node.right:
                    bfs_queue.append(curr_node.right)
                pos += 1
            output.append(this_batch)
        return output
