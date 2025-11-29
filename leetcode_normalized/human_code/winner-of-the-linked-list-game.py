class C1(object):

    def gameResult(self, a1):
        """
        """
        v1 = 0
        while a1:
            v1 += cmp(a1.val, a1.next.val)
            a1 = a1.next.__next__
        return 'Tie' if v1 == 0 else 'Odd' if v1 < 0 else 'Even'
