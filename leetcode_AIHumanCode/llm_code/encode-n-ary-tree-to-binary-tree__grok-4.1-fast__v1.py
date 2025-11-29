class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):

    def encode(self, root):
        def build_sibling_chain(nodes):
            if not nodes:
                return None
            curr = nodes[0]
            bt = TreeNode(curr.val)
            bt.right = build_sibling_chain(curr.children)
            bt.left = build_sibling_chain(nodes[1:])
            return bt
        return build_sibling_chain([root]) if root else None

    def decode(self, data):
        def extract_children(broot):
            childs = []
            curr_b = broot
            while curr_b:
                childs.append(reconstruct(curr_b))
                curr_b = curr_b.left
            return childs

        def reconstruct(bnode):
            if not bnode:
                return None
            nary = Node(bnode.val, [])
            nary.children = extract_children(bnode.right)
            return nary
        return reconstruct(data)
