# Time:  O(n)
# Space: O()
import collections


class Solution2(object):
    def findBottomLeftValue(self, root):
        """
        """
        last_node, q = None, collections.deque([root])
        while q:
            last_node = q.popleft()
            q.extend([n for n in [last_node.right, last_node.left] if n])
        return last_node.val

