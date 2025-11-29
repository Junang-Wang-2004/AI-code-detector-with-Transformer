class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        stk = [(root, str(root.val))]
        paths = []
        while stk:
            curr, pth = stk.pop()
            if not curr.left and not curr.right:
                paths.append(pth)
            if curr.right:
                stk.append((curr.right, pth + "->" + str(curr.right.val)))
            if curr.left:
                stk.append((curr.left, pth + "->" + str(curr.left.val)))
        return paths
