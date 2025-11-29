import collections
import itertools

class C1(object):

    def __init__(self, a1, a2, a3):
        """
        """
        self.__lookup = {k: v for v1, v2 in zip(a1, a2)}
        self.__cnt = collections.Counter((self.encrypt(x) for v3 in a3))

    def encrypt(self, a1):
        """
        """
        if any((c not in self.__lookup for v1 in a1)):
            return ''
        return ''.join((self.__lookup[v1] for v1 in a1))

    def decrypt(self, a1):
        """
        """
        return self.__cnt[a1]
