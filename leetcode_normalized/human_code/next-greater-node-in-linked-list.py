class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C2(object):

    def nextLargerNodes(self, a1):
        """
        """
        v1, v2 = ([], [])
        while a1:
            while v2 and v2[-1][1] < a1.val:
                v1[v2.pop()[0]] = a1.val
            v2.append([len(v1), a1.val])
            v1.append(0)
            a1 = a1.__next__
        return v1
