class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def removeElements(self, a1, a2):
        v1 = C1(float('-inf'))
        v1.next = a1
        v2, v3 = (v1, v1.__next__)
        while v3:
            if v3.val == a2:
                v2.next = v3.__next__
            else:
                v2 = v3
            v3 = v3.__next__
        return v1.__next__
