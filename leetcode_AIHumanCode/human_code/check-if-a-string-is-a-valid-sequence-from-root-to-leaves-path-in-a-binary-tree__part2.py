# Time:  O(n)
# Space: O(h)
# dfs solution with stack
class Solution2(object):
    def isValidSequence(self, root, arr):
        """
        """
        s = [(root, 0)]
        while s:
            node, depth = s.pop()
            if not node or depth == len(arr) or node.val != arr[depth]:
                continue
            if depth+1 == len(arr) and node.left == node.right:
                return True
            s.append((node.right, depth+1))
            s.append((node.left, depth+1))
        return False


