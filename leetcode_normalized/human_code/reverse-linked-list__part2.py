class C1(object):

    def reverseList(self, a1):
        [v1, v2] = self.reverseListRecu(a1)
        return v1

    def reverseListRecu(self, a1):
        if not a1:
            return [None, None]
        [v1, v2] = self.reverseListRecu(a1.__next__)
        if v2:
            v2.next = a1
            a1.next = None
            return [v1, a1]
        else:
            return [a1, a1]
