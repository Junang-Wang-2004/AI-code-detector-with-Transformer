from functools import reduce

class C1(object):

    def countPermutations(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def factorial(a1):
            return reduce(lambda accu, x: accu * x % v1, range(1, a1 + 1), 1)
        return factorial(len(a1) - 1) if all((a1[0] < a1[i] for v2 in range(1, len(a1)))) else 0
