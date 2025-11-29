class C1(object):

    def isPalindrome(self, a1):
        v1, v2 = (None, a1)
        while v2 and v2.__next__:
            v2 = v2.next.__next__
            a1.next, v1, a1 = (v1, a1, a1.next)
        v4 = a1.__next__ if v2 else a1
        v5 = True
        while v1:
            v5 = v5 and v1.val == v4.val
            v1.next, a1, v1 = (a1, v1, v1.next)
            v4 = v4.__next__
        return v5
