import collections

class C1(object):

    def sortString(self, a1):
        """
        """
        v1, v2, v3 = ([], collections.Counter(a1), False)
        while v2:
            for v4 in sorted(list(v2.keys()), reverse=v3):
                v1.append(v4)
                v2[v4] -= 1
                if not v2[v4]:
                    del v2[v4]
            v3 = not v3
        return ''.join(v1)
