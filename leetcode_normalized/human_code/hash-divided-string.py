from functools import reduce

class C1(object):

    def stringHash(self, a1, a2):
        """
        """
        v1 = (chr(ord('a') + reduce(lambda accu, x: (accu + x) % 26, (ord(a1[i + j]) - ord('a') for v2 in range(a2)), 0)) for v3 in range(0, len(a1), a2))
        return ''.join(v1)
