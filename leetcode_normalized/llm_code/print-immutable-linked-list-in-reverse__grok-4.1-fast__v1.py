class C1(object):

    def printLinkedListInReverse(self, a1):
        """
        """
        v1 = []
        v2 = a1
        while v2:
            v1.append(v2)
            v2 = v2.getNext()
        while v1:
            v1.pop().printValue()
