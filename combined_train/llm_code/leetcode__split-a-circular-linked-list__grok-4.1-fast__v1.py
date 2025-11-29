class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def splitCircularLinkedList(self, a1):
        v1 = 1
        v2 = a1.next
        while v2 != a1:
            v2 = v2.next
            v1 += 1
        v3 = v1 // 2
        v4 = a1
        for v5 in range(v3 - 1):
            v4 = v4.next
        v6 = v4.next
        v4.next = a1
        v2 = v6
        while v2.next != a1:
            v2 = v2.next
        v2.next = v6
        return [a1, v6]
