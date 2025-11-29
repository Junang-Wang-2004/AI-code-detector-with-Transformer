class C1(object):

    def losingPlayer(self, a1, a2):
        """
        """
        return 'Alice' if min(a1, a2 // 4) % 2 else 'Bob'
