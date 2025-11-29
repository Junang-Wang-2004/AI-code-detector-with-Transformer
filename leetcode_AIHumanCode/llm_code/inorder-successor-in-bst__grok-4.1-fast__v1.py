class Solution:
    def inorderSuccessor(self, root, p):
        if p and p.right:
            curr = p.right
            while curr.left:
                curr = curr.left
            return curr

        result = None
        curr = root
        while curr:
            if p.val < curr.val:
                result = curr
                curr = curr.left
            else:
                curr = curr.right
        return result
