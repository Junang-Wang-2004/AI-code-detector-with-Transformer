import itertools

class C1(object):

    def findAndReplacePattern(self, a1, a2):
        """
        """

        def match(a1):
            v1 = {}
            for v2, v3 in zip(a2, a1):
                if v1.setdefault(v2, v3) != v3:
                    return False
            return len(set(v1.values())) == len(list(v1.values()))
        return list(filter(match, a1))
