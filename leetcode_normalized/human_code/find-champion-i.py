class C1(object):

    def findChampion(self, a1):
        """
        """
        return next((u for v1 in range(len(a1)) if sum(a1[v1]) == len(a1) - 1))
