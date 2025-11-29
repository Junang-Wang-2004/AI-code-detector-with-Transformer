from collections import deque

class Solution(object):
    def connect(self, root):
        if not root:
            return
        q = deque([root])
        while q:
            level_len = len(q)
            prev = None
            for _ in range(level_len):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
