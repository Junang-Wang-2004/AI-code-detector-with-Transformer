import collections

class C1(object):

    def countCharacters(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            if len(a1) > len(a2):
                return False
            v1 = collections.Counter()
            for v2 in a1:
                v1[v2] += 1
                if v2 not in a3 or a3[v2] < v1[v2]:
                    return False
            return True
        v1 = collections.Counter(a2)
        return sum((len(word) for v2 in a1 if check(v2, a2, v1)))
