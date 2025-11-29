class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def pairSum(self, a1):
        """
        """

        def reverseList(a1):
            v1 = C1()
            while a1:
                v1.next, a1.next, a1 = (a1, v1.next, a1.next)
            return v1.__next__
        v1 = C1(next=a1)
        v2 = v3 = v1
        while v3.__next__ and v3.next.__next__:
            v2, v3 = (v2.__next__, v3.next.__next__)
        v4 = 0
        v5 = reverseList(v2)
        while a1:
            v4 = max(v4, a1.val + v5.val)
            a1, v5 = (a1.__next__, v5.__next__)
        return v4
