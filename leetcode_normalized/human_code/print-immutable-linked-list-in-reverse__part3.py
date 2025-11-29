class C1(object):

    def printLinkedListInReverse(self, a1):
        """
        """
        v1 = None
        while a1 != v1:
            v2 = a1
            while v2.getNext() != v1:
                v2 = v2.getNext()
            v2.printValue()
            v1 = v2
