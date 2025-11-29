# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        self.sequence = []
        temp_stack = []
        current = root
        while current or temp_stack:
            while current:
                temp_stack.append(current)
                current = current.left
            current = temp_stack.pop()
            self.sequence.append(current.val)
            current = current.right
        self.pointer = -1

    def hasNext(self):
        return self.pointer < len(self.sequence) - 1

    def __next__(self):
        self.pointer += 1
        return self.sequence[self.pointer]

    def hasPrev(self):
        return self.pointer > 0

    def prev(self):
        self.pointer -= 1
        return self.sequence[self.pointer]
