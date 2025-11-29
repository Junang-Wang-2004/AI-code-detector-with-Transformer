class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:
    def __init__(self, root):
        self.root = root

    def find(self, target):
        node = self.root
        temp = target
        moves = []
        while temp > 0:
            moves.append(temp % 2 == 0)
            temp = (temp - 1) // 2
        for go_right in reversed(moves):
            if go_right:
                if not node or not node.right:
                    return False
                node = node.right
            else:
                if not node or not node.left:
                    return False
                node = node.left
        return node is not None
