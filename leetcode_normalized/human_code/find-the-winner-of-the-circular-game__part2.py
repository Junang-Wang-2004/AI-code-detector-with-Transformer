from functools import reduce

class C1(object):

    def findTheWinner(self, a1, a2):
        """
        """

        def f(a1, a2, a3):
            if a2 == 1:
                return 0
            return (a3 + f((a1 + a3) % a2, a2 - 1, a3)) % a2
        return f(0, a1, a2) + 1
