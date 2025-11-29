class C1(object):

    def monkeyMove(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        return (pow(2, a1, v1) - 2) % v1
