class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def countNodes(self, a1):
        """
        """

        def height(a1):
            v1 = -1
            while a1:
                v1 += 1
                a1 = a1.left
            return v1
        v1, v2 = (0, height(a1))
        while a1:
            if height(a1.right) == v2 - 1:
                v1 += 2 ** v2
                a1 = a1.right
            else:
                v1 += 2 ** (v2 - 1)
                a1 = a1.left
            v2 -= 1
        return v1
