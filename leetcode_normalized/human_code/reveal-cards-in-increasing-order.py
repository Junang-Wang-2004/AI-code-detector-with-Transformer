import collections

class C1(object):

    def deckRevealedIncreasing(self, a1):
        """
        """
        v1 = collections.deque()
        a1.sort(reverse=True)
        for v2 in a1:
            if v1:
                v1.appendleft(v1.pop())
            v1.appendleft(v2)
        return list(v1)
