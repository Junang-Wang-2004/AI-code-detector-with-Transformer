class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def balanceBST(self, a1):
        v1 = []
        v2 = a1
        v3 = []
        while v2 or v3:
            while v2:
                v3.append(v2)
                v2 = v2.left
            v2 = v3.pop()
            v1.append(v2.val)
            v2 = v2.right

        def build_tree(a1, a2):
            if a1 >= a2:
                return None
            v1 = (a1 + a2) // 2
            v2 = C1(v1[v1])
            v2.left = build_tree(a1, v1)
            v2.right = build_tree(v1 + 1, a2)
            return v2
        return build_tree(0, len(v1))
