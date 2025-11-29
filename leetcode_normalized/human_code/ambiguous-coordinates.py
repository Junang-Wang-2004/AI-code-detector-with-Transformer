import itertools

class C1(object):

    def ambiguousCoordinates(self, a1):
        """
        """

        def make(a1, a2, a3):
            for v1 in range(1, a3 + 1):
                v2 = a1[a2:a2 + v1]
                v3 = a1[a2 + v1:a2 + a3]
                if (not v2.startswith('0') or v2 == '0') and (not v3.endswith('0')):
                    yield ''.join([v2, '.' if v3 else '', v3])
        return ['({}, {})'.format(*cand) for v1 in range(1, len(a1) - 2) for v2 in itertools.product(make(a1, 1, v1), make(a1, v1 + 1, len(a1) - 2 - v1))]
