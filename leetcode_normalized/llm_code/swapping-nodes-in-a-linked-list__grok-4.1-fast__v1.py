class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def swapNodes(self, a1, a2):
        v1 = a1
        for v2 in range(a2 - 1):
            v1 = v1.next
        v3 = a1
        v4 = v1
        while v4.next:
            v4 = v4.next
            v3 = v3.next
        v1.val, v3.val = (v3.val, v1.val)
        return a1
