class C1(object):

    def printLinkedListInReverse(self, a1):
        """
        """
        v1 = []
        while a1:
            v1.append(a1)
            a1 = a1.getNext()
        for v3 in reversed(v1):
            v3.printValue()
