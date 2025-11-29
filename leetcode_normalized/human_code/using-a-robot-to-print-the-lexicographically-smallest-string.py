import collections

class C1(object):

    def robotWithString(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2, v3 = ([], [])
        v4 = 'a'
        for v5 in a1:
            v3.append(v5)
            v1[v5] -= 1
            while v4 < 'z' and v1[v4] == 0:
                v4 = chr(ord(v4) + 1)
            while v3 and v3[-1] <= v4:
                v2.append(v3.pop())
        return ''.join(v2)
