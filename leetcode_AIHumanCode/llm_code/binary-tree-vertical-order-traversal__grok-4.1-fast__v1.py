from collections import deque

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        vert_map = {}
        bfs = deque([(root, 0)])
        while bfs:
            curr, idx = bfs.popleft()
            vert_map.setdefault(idx, []).append(curr.val)
            if curr.left:
                bfs.append((curr.left, idx - 1))
            if curr.right:
                bfs.append((curr.right, idx + 1))
        ordered_cols = sorted(vert_map)
        return [vert_map[c] for c in ordered_cols]
