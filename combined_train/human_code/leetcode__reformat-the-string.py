import collections

class C1(object):

    def reformat(self, a1):
        """
        """

        def char_gen(a1, a2, a3):
            for v1 in range(ord(a1), ord(a2) + 1):
                v1 = chr(v1)
                for v2 in range(a3[v1]):
                    yield v1
            yield ''
        v1 = collections.defaultdict(int)
        v2 = 0
        for v3 in a1:
            v1[v3] += 1
            if v3.isalpha():
                v2 += 1
        if abs(len(a1) - 2 * v2) > 1:
            return ''
        v4 = []
        v5, v6 = (char_gen('a', 'z', v1), char_gen('0', '9', v1))
        if v2 < len(a1) - v2:
            v5, v6 = (v6, v5)
        while len(v4) < len(a1):
            v4.append(next(v5))
            v4.append(next(v6))
        return ''.join(v4)
