class Solution(object):
    def getKthCharacter(self, root, k):
        if root.len == 0:
            return root.val[k - 1]
        left_size = 0
        if root.left:
            left_size = root.left.len if root.left.len > 0 else len(root.left.val)
        if k <= left_size:
            return self.getKthCharacter(root.left, k)
        return self.getKthCharacter(root.right, k - left_size)
