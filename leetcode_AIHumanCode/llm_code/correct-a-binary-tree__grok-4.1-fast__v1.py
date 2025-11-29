from collections import deque

class Solution:
    def correctBinaryTree(self, root):
        q = deque([(root, None)])
        while q:
            curr_size = len(q)
            level_data = []
            for _ in range(curr_size):
                curr_node, prev_node = q.popleft()
                level_data.append((curr_node, prev_node))
            level_nodes = {nd for nd, _ in level_data}
            for curr_node, prev_node in level_data:
                if curr_node.right in level_nodes:
                    if prev_node.left == curr_node:
                        prev_node.left = None
                    else:
                        prev_node.right = None
                    return root
                if curr_node.left:
                    q.append((curr_node.left, curr_node))
                if curr_node.right:
                    q.append((curr_node.right, curr_node))
