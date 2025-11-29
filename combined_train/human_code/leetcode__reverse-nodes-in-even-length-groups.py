class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def reverseEvenLengthGroups(self, a1):
        """
        """
        v1, v2 = (a1, 2)
        while v1.__next__:
            v3, v4 = (v1, 0)
            for v5 in range(v2):
                if not v3.__next__:
                    break
                v4 += 1
                v3 = v3.__next__
            v2 += 1
            if v4 % 2:
                v1 = v3
                continue
            v3, v6 = (v1.__next__, None)
            for v5 in range(v4):
                v3.next, v3, v6 = (v6, v3.next, v3)
            v1.next.next, v1.next, v1 = (v3, v6, v1.next)
        return a1
