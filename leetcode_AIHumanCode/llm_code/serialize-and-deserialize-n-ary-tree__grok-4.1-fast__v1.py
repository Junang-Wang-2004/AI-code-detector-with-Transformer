class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Codec(object):

    def serialize(self, root):
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        parts = []
        def traverse(curr):
            parts.append(str(curr.val))
            parts.append(str(len(curr.children)))
            for kid in curr.children:
                traverse(kid)
        traverse(root)
        return " ".join(parts)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        queue = iter(data.split())
        def build():
            value = next(queue)
            node = Node(int(value), [])
            count = int(next(queue))
            for _ in range(count):
                child_node = build()
                node.children.append(child_node)
            return node
        return build()
