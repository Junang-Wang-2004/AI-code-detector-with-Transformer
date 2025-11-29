# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution2(object):
    def postorderTraversal(self, root):
        """
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root, True))
                stack.append((root.right, False))
                stack.append((root.left, False))
        return result

