class C1(object):

    def mostVisited(self, a1, a2):
        """
        """
        return list(range(a2[0], a2[-1] + 1)) or list(range(1, a2[-1] + 1)) + list(range(a2[0], a1 + 1))
