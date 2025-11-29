class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C3(object):

    def encode(self, a1):
        """Encodes an n-ary tree to a binary tree.
        
        """

        def encodeHelper(a1, a2, a3):
            if not a1:
                return None
            v1 = C2(a1.val)
            if a3 + 1 < len(a2.children):
                v1.left = encodeHelper(a2.children[a3 + 1], a2, a3 + 1)
            if a1.children:
                v1.right = encodeHelper(a1.children[0], a1, 0)
            return v1
        if not a1:
            return None
        v1 = C2(a1.val)
        if a1.children:
            v1.right = encodeHelper(a1.children[0], a1, 0)
        return v1

    def decode(self, a1):
        """Decodes your binary tree to an n-ary tree.
        
        """

        def decodeHelper(a1, a2):
            if not a1:
                return
            v1 = []
            v2 = C1(a1.val, v1)
            decodeHelper(a1.right, v2)
            a2.children.append(v2)
            decodeHelper(a1.left, a2)
        if not a1:
            return None
        v1 = []
        v2 = C1(a1.val, v1)
        decodeHelper(a1.right, v2)
        return v2
