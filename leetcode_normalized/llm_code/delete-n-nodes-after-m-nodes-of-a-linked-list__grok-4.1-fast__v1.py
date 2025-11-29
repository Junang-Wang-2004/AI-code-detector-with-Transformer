class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def deleteNodes(self, a1, a2, a3):
        v1 = C1(next=a1)
        v2 = v1
        while v2.next:
            v3 = 0
            while v3 < a2 and v2.next:
                v2 = v2.next
                v3 += 1
            v4 = v2.next
            v5 = 0
            while v5 < a3 and v4:
                v4 = v4.next
                v5 += 1
            v2.next = v4
        return v1.next
