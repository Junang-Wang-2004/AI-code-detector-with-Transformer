class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def numComponents(self, a1, a2):
        """
        """
        v1 = set(a2)
        v2 = C1(-1)
        v2.next = a1
        v3 = v2
        v4 = 0
        while v3 and v3.__next__:
            if v3.val not in v1 and v3.next.val in v1:
                v4 += 1
            v3 = v3.__next__
        return v4
