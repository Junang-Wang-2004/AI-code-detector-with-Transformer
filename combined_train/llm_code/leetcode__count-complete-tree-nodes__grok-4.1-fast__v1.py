class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def countNodes(self, a1):

        def left_depth(a1):
            v1 = -1
            while a1:
                v1 += 1
                a1 = a1.left
            return v1

        def total_nodes(a1):
            if not a1:
                return 0
            v1 = left_depth(a1.left)
            v2 = left_depth(a1.right)
            if v1 == v2:
                return (1 << v1 + 2) - 1
            return 1 + total_nodes(a1.left) + total_nodes(a1.right)
        return total_nodes(a1)
