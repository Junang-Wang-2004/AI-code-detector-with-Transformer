class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def serialize(self, a1):

        def preorder(a1):
            if a1 is None:
                return '#'
            return f'{a1.val} {preorder(a1.left)} {preorder(a1.right)}'
        return preorder(a1)

    def deserialize(self, a1):
        v1 = a1.split()
        v2 = [0]

        def construct():
            if v1[v2[0]] == '#':
                v2[0] += 1
                return None
            v1 = int(v1[v2[0]])
            v2[0] += 1
            v2 = C1(v1)
            v2.left = construct()
            v2.right = construct()
            return v2
        return construct()
