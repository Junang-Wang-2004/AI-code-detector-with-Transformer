class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def preorder(node):
            if node is None:
                return '#'
            return f"{node.val} {preorder(node.left)} {preorder(node.right)}"
        return preorder(root)

    def deserialize(self, data):
        tokens = data.split()
        idx = [0]

        def construct():
            if tokens[idx[0]] == '#':
                idx[0] += 1
                return None
            val = int(tokens[idx[0]])
            idx[0] += 1
            node = TreeNode(val)
            node.left = construct()
            node.right = construct()
            return node
        return construct()
