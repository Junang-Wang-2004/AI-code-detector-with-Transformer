class C1(object):

    def __init__(self, a1=0, a2=None):
        self.val = a1
        self.next = a2

class C2(object):

    def nodesBetweenCriticalPoints(self, a1):
        """
        """
        v1 = v2 = -1
        v3 = float('inf')
        v4, v5, a1 = (0, a1.val, a1.__next__)
        while a1.__next__:
            if max(v5, a1.next.val) < a1.val or min(v5, a1.next.val) > a1.val:
                if v1 == -1:
                    v1 = v4
                if v2 != -1:
                    v3 = min(v3, v4 - v2)
                v2 = v4
            v4 += 1
            v5 = a1.val
            a1 = a1.__next__
        return [v3, v2 - v1] if v2 != v1 else [-1, -1]
