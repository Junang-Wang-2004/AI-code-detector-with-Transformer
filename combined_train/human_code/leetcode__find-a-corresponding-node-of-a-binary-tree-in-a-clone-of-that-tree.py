import itertools

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def getTargetCopy(self, a1, a2, a3):
        """
        """

        def preorder_gen(a1):
            v1 = [a1]
            while v1:
                a1 = v1.pop()
                if not a1:
                    continue
                yield a1
                v1.append(a1.right)
                v1.append(a1.left)
        for v1, v2 in zip(preorder_gen(a1), preorder_gen(a2)):
            if v1 == a3:
                return v2
