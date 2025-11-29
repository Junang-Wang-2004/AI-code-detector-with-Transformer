class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def flipEquiv(self, a1, a2):

        def canon(a1):
            if a1 is None:
                return ()
            v1 = canon(a1.left)
            v2 = canon(a1.right)
            return (a1.val, tuple(sorted((v1, v2))))
        return canon(a1) == canon(a2)
