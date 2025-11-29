class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def serialize(self, a1):
        """Encodes a tree to a single string.
        """
        if not a1:
            return ''
        v1 = []

        def traverse(a1):
            v1.append(str(a1.val))
            v1.append(str(len(a1.children)))
            for v1 in a1.children:
                traverse(v1)
        traverse(a1)
        return ' '.join(v1)

    def deserialize(self, a1):
        """Decodes your encoded data to tree.
        """
        if not a1:
            return None
        v1 = iter(a1.split())

        def build():
            v1 = next(v1)
            v2 = C1(int(v1), [])
            v3 = int(next(v1))
            for v4 in range(v3):
                v5 = build()
                v2.children.append(v5)
            return v2
        return build()
