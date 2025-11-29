import random

def f1():
    return random.randint(1, 7)

class C1(object):

    def __init__(self):
        self.__cache = []

    def rand10(self):
        """
        """

        def generate(a1):
            v1 = 32
            v2 = sum(((f1() - 1) * 7 ** i for v3 in range(v1)))
            v4 = 7 ** v1
            while v2 < v4 // 10 * 10:
                a1.append(v2 % 10 + 1)
                v2 /= 10
                v4 /= 10
        while not self.__cache:
            generate(self.__cache)
        return self.__cache.pop()
