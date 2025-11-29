class C1(object):

    def __init__(self, a1, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def insert(self, a1, a2):
        if not a1:
            v1 = C1(a2, None)
            v1.next = v1
            return v1
        v2 = C1(a2, None)
        v3 = a1
        v4 = a1
        v5 = a1.next
        while v5 != v3:
            if v4.val > v5.val:
                if a2 >= v4.val or a2 <= v5.val:
                    break
            if v4.val <= a2 < v5.val:
                break
            v4 = v5
            v5 = v5.next
        v4.next = v2
        v2.next = v5
        return a1
