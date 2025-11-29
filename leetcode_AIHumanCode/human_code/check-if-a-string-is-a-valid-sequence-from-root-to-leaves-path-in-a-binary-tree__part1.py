# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs solution
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        """
        q = [root]
        for depth in range(len(arr)):
            new_q = []
            while q:
                node = q.pop()
                if not node or node.val != arr[depth]:
                    continue
                if depth+1 == len(arr) and node.left == node.right:
                    return True
                new_q.extend(child for child in (node.left, node.right))
            q = new_q
        return False


