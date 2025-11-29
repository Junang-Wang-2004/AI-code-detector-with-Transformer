class C1(object):

    def kidsWithCandies(self, a1, a2):
        """
        """
        v1 = max(a1)
        return [x + a2 >= v1 for v2 in a1]
