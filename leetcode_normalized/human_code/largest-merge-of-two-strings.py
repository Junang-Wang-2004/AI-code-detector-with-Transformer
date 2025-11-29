import collections

class C1(object):

    def largestMerge(self, a1, a2):
        """
        """
        v1 = collections.deque(a1)
        v2 = collections.deque(a2)
        v3 = []
        while v1 or v2:
            if v1 > v2:
                v3.append(v1.popleft())
            else:
                v3.append(v2.popleft())
        return ''.join(v3)
