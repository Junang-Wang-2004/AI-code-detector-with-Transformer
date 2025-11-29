class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def mergeInBetween(self, a1, a2, a3, a4):
        v1 = C1(0)
        v1.next = a1
        v2 = v1
        for v3 in range(a2):
            v2 = v2.next
        v4 = v2.next
        for v3 in range(a3 - a2 + 1):
            v4 = v4.next
        v2.next = a4
        v5 = a4
        while v5.next:
            v5 = v5.next
        v5.next = v4
        return v1.next
