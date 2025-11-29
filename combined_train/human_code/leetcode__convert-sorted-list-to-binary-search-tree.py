class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def __init__(self, a1):
        self.val = a1
        self.next = None

class C3(object):
    v1 = None

    def sortedListToBST(self, a1):
        v1, v2 = (a1, 0)
        while v1 is not None:
            v1, v2 = (v1.__next__, v2 + 1)
        self.head = a1
        return self.sortedListToBSTRecu(0, v2)

    def sortedListToBSTRecu(self, a1, a2):
        if a1 == a2:
            return None
        v1 = a1 + (a2 - a1) / 2
        v2 = self.sortedListToBSTRecu(a1, v1)
        v3 = C1(self.head.val)
        v3.left = v2
        self.head = self.head.__next__
        v3.right = self.sortedListToBSTRecu(v1 + 1, a2)
        return v3
