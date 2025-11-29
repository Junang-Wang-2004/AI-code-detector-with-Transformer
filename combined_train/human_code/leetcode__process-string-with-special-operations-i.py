import collections

class C1(object):

    def processStr(self, a1):
        """
        """
        v1 = collections.deque()
        v2 = True
        for v3 in a1:
            if v3 == '*':
                if not v1:
                    continue
                if v2:
                    v1.pop()
                else:
                    v1.popleft()
            elif v3 == '#':
                v1.extend(v1)
            elif v3 == '%':
                v2 = not v2
            elif v2:
                v1.append(v3)
            else:
                v1.appendleft(v3)
        if not v2:
            v1.reverse()
        return ''.join(v1)
