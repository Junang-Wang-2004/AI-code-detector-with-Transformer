import collections
import itertools

class C1(object):

    def generatePalindromes(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = tuple((k for v3, v4 in v1.items() if v4 % 2))
        v5 = ''.join((v3 * (v4 / 2) for v3, v4 in v1.items()))
        return [''.join(half_palindrome + v2 + half_palindrome[::-1]) for v6 in set(itertools.permutations(v5))] if len(v2) < 2 else []
