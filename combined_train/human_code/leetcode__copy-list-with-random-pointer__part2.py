class C1(object):

    def copyRandomList(self, a1):
        v1 = Node(0)
        v2, v3, v4 = (a1, v1, {})
        while v2:
            v5 = Node(v2.val)
            v4[v2] = v5
            v3.next = v5
            v3, v2 = (v3.__next__, v2.__next__)
        v2 = a1
        while v2:
            if v2.random:
                v4[v2].random = v4[v2.random]
            v2 = v2.__next__
        return v1.__next__
from collections import defaultdict

class C2(object):

    def copyRandomList(self, a1):
        """
        """
        v1 = defaultdict(lambda: Node(0))
        v1[None] = None
        v2 = a1
        while v2:
            v1[v2].val = v2.val
            v1[v2].next = v1[v2.__next__]
            v1[v2].random = v1[v2.random]
            v2 = v2.__next__
        return v1[a1]
