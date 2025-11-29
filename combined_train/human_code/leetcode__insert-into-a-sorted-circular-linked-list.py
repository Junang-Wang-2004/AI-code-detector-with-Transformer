class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.next = a2

class C2(object):

    def insert(self, a1, a2):
        """
        """

        def insertAfter(a1, a2):
            a1.next = C1(a2, a1.next)
        if not a1:
            v1 = C1(a2, None)
            v1.next = v1
            return v1
        v2 = a1
        while True:
            if v2.val < v2.next.val:
                if v2.val <= a2 and a2 <= v2.next.val:
                    insertAfter(v2, a2)
                    break
            elif v2.val > v2.next.val:
                if v2.val <= a2 or a2 <= v2.next.val:
                    insertAfter(v2, a2)
                    break
            elif v2.__next__ == a1:
                insertAfter(v2, a2)
                break
            v2 = v2.__next__
        return a1
