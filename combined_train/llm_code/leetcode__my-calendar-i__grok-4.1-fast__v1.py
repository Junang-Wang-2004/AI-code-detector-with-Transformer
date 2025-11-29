class C1:

    def __init__(self, a1, a2):
        self.s = a1
        self.e = a2
        self.lchild = None
        self.rchild = None

class C2:

    def __init__(self):
        self.root = None

    def book(self, a1, a2):
        if self.root is None:
            self.root = C1(a1, a2)
            return True
        v1 = C1(a1, a2)
        v2 = self.root
        while True:
            if a1 >= v2.e:
                if v2.rchild is None:
                    v2.rchild = v1
                    return True
                v2 = v2.rchild
            elif a2 <= v2.s:
                if v2.lchild is None:
                    v2.lchild = v1
                    return True
                v2 = v2.lchild
            else:
                return False
