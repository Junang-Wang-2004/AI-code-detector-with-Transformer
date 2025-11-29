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

        def build_sibling_chain(a1):
            if not a1:
                return None
            v1 = a1[0]
            v2 = C2(v1.val)
            v2.right = build_sibling_chain(v1.children)
            v2.left = build_sibling_chain(a1[1:])
            return v2
        return build_sibling_chain([a1]) if a1 else None

    def decode(self, a1):

        def extract_children(a1):
            v1 = []
            v2 = a1
            while v2:
                v1.append(reconstruct(v2))
                v2 = v2.left
            return v1

        def reconstruct(a1):
            if not a1:
                return None
            v1 = C1(a1.val, [])
            v1.children = extract_children(a1.right)
            return v1
        return reconstruct(a1)
