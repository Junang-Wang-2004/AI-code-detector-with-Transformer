import random

class C1(object):

    def __init__(self):
        self.__random_length = 6
        self.__tiny_url = 'http://tinyurl.com/'
        self.__alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__lookup = {}

    def encode(self, a1):
        """Encodes a URL to a shortened URL.

        """

        def getRand():
            v1 = []
            for v2 in range(self.__random_length):
                v1 += self.__alphabet[random.randint(0, len(self.__alphabet) - 1)]
            return ''.join(v1)
        v1 = getRand()
        while v1 in self.__lookup:
            v1 = getRand()
        self.__lookup[v1] = a1
        return self.__tiny_url + v1

    def decode(self, a1):
        """Decodes a shortened URL to its original URL.

        """
        return self.__lookup[a1[len(self.__tiny_url):]]
from hashlib import sha256

class C2(object):

    def __init__(self):
        self._cache = {}
        self.url = 'http://tinyurl.com/'

    def encode(self, a1):
        """Encodes a URL to a shortened URL.

        """
        v1 = sha256(a1.encode()).hexdigest()[:6]
        self._cache[v1] = a1
        return self.url + v1

    def decode(self, a1):
        """Decodes a shortened URL to its original URL.

        """
        v1 = a1.replace(self.url, '')
        return self._cache[v1]
