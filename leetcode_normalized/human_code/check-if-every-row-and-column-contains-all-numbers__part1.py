from functools import reduce

class C1(object):

    def checkValid(self, a1):
        """
        """
        return all((len(set(row)) == len(a1) for v1 in a1)) and all((len(set((a1[i][j] for v2 in range(len(a1))))) == len(a1) for v3 in range(len(a1[0]))))
