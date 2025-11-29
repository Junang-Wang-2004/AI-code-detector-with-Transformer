class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = self.right = None


class BSTIterator(object):
    def __init__(self, root):
        self.path = []
        curr = root
        while curr:
            self.path.append(curr)
            curr = curr.left

    def hasNext(self):
        return len(self.path) > 0

    def __next__(self):
        node = self.path.pop()
        right = node.right
        while right:
            self.path.append(right)
            right = right.left
        return node.val
