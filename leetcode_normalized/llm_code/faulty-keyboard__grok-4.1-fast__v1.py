import collections

class C1:

    def finalString(self, a1):
        v1 = collections.deque()
        v2 = False
        for v3 in a1:
            if v3 != 'i':
                if v2:
                    v1.appendleft(v3)
                else:
                    v1.append(v3)
            else:
                v2 = not v2
        if v2:
            v1.reverse()
        return ''.join(v1)
