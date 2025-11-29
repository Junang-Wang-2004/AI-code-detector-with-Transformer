# Time:  O(n)
# Space: O(w)
class Solution2(object):
    def isCompleteTree(self, root):
        """
        """
        prev_level, current = [], [(root, 1)]
        count = 0
        while current:
            count += len(current)
            next_level = []
            for node, v in current:
                if not node:
                    continue
                next_level.append((node.left, 2*v))
                next_level.append((node.right, 2*v+1))
            prev_level, current = current, next_level
        return prev_level[-1][1] == count
