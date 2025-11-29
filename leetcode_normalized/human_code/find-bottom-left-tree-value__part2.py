import collections

class C1(object):

    def findBottomLeftValue(self, a1):
        """
        """
        v1, v2 = (None, collections.deque([a1]))
        while v2:
            v1 = v2.popleft()
            v2.extend([n for v3 in [v1.right, v1.left] if v3])
        return v1.val
