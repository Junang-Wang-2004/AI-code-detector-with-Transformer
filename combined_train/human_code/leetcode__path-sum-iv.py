import collections

class C1(object):

    def pathSum(self, a1):
        """
        """

        class Node(object):

            def __init__(self, a1):
                self.level = a1 / 100 - 1
                self.i = a1 % 100 / 10 - 1
                self.val = a1 % 10
                self.leaf = True

            def isParent(self, a1):
                return self.level == a1.level - 1 and self.i == a1.i / 2
        if not a1:
            return 0
        v1 = 0
        v2 = collections.deque()
        v3 = Node(10)
        v4 = v3
        for v5 in a1:
            v6 = Node(v5)
            while not v4.isParent(v6):
                v1 += v4.val if v4.leaf else 0
                v4 = v2.popleft()
            v4.leaf = False
            v6.val += v4.val
            v2.append(v6)
        while v2:
            v1 += v2.pop().val
        return v1
