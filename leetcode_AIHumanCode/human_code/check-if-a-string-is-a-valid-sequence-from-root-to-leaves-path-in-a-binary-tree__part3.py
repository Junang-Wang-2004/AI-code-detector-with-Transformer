# Time:  O(n)
# Space: O(h)
# dfs solution with recursion
class Solution3(object):
    def isValidSequence(self, root, arr):
        """
        """
        def dfs(node, arr, depth):
            if not node or depth == len(arr) or node.val != arr[depth]:
                return False
            if depth+1 == len(arr) and node.left == node.right:
                return True
            return dfs(node.left, arr, depth+1) or dfs(node.right, arr, depth+1)

        return dfs(root, arr, 0)
