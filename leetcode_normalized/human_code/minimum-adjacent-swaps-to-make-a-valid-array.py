class C1(object):

    def minimumSwaps(self, a1):
        """
        """
        v1 = min(range(len(a1)), key=a1.__getitem__)
        v2 = max(reversed(range(len(a1))), key=a1.__getitem__)
        return len(a1) - 1 - v2 + v1 - int(v2 < v1)
