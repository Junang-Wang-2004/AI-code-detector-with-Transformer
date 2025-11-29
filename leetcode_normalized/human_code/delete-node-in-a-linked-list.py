class C1(object):

    def deleteNode(self, a1):
        if a1 and a1.__next__:
            v1 = a1.__next__
            a1.val = v1.val
            a1.next = v1.__next__
            del v1
