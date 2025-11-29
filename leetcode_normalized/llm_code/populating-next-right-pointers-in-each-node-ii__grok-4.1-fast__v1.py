class C1:

    def __init__(self, a1=0, a2=None, a3=None, a4=None):
        self.val = a1
        self.left = a2
        self.right = a3
        self.next = a4

class C2:

    def connect(self, a1):
        if not a1:
            return a1
        v1 = a1
        while v1 and v1.left:
            v2 = v1
            while v2:
                v2.left.next = v2.right
                if v2.next:
                    v2.right.next = v2.next.left
                v2 = v2.next
            v1 = v1.left
        return a1
