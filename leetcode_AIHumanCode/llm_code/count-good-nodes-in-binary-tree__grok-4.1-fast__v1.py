from collections import deque

class Solution(object):
    def goodNodes(self, root):
        if not root:
            return 0
        queue = deque([(root, root.val)])
        total = 0
        while queue:
            current, pathmax = queue.popleft()
            if current.val >= pathmax:
                total += 1
            updatemax = max(pathmax, current.val)
            if current.left:
                queue.append((current.left, updatemax))
            if current.right:
                queue.append((current.right, updatemax))
        return total
