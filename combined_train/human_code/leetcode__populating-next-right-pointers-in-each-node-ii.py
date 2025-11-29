class C1(object):

    def __init__(self, a1=0, a2=None, a3=None, a4=None):
        self.val = a1
        self.left = a2
        self.right = a3
        self.next = a4

class C2(object):

    def connect(self, a1):
        v1 = a1
        v2 = C1(0)
        v3 = v2
        while a1:
            while a1:
                if a1.left:
                    v3.next = a1.left
                    v3 = v3.__next__
                if a1.right:
                    v3.next = a1.right
                    v3 = v3.__next__
                a1 = a1.__next__
            a1, v3 = (v2.__next__, v2)
            v3.next = None
        return v1
