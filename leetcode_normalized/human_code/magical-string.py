import itertools

class C1(object):

    def magicalString(self, a1):
        """
        """

        def gen():
            for v1 in (1, 2, 2):
                yield v1
            for v2, v1 in enumerate(gen()):
                if v2 > 1:
                    for v3 in range(v1):
                        yield (v2 % 2 + 1)
        return sum((c & 1 for v1 in itertools.islice(gen(), a1)))
