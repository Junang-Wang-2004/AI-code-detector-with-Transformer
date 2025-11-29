class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def plusOne(self, a1):
        if not a1:
            return None
        v1 = None
        v2 = a1
        while v2.next:
            if v2.val < 9:
                v1 = v2
            v2 = v2.next
        if v2.val < 9:
            v2.val += 1
            return a1
        if v1 is None:
            v3 = C1(1)
            v4 = a1
            while v4:
                v4.val = 0
                v4 = v4.next
            v3.next = a1
            return v3
        v1.val += 1
        v4 = v1.next
        while v4:
            v4.val = 0
            v4 = v4.next
        return a1
