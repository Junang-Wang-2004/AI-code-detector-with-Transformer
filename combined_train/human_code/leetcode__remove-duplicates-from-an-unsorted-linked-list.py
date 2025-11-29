import collections

class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def deleteDuplicatesUnsorted(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = a1
        while v2:
            v1[v2.val] += 1
            v2 = v2.__next__
        v2 = v3 = C1(0, a1)
        while v2.__next__:
            if v1[v2.next.val] == 1:
                v2 = v2.__next__
            else:
                v2.next = v2.next.__next__
        return v3.__next__
