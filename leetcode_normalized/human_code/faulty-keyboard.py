import collections

class C1(object):

    def finalString(self, a1):
        """
        """
        v1 = collections.deque()
        v2 = 0
        for v3 in a1:
            if v3 == 'i':
                v2 ^= 1
            else:
                v1.appendleft(v3) if v2 else v1.append(v3)
        if v2:
            v1.reverse()
        return ''.join(v1)
