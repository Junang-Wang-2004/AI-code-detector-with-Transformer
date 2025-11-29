class C1(object):

    def sumOfGoodNumbers(self, a1, a2):
        """
        """
        return sum((a1[i] for v1 in range(len(a1)) if (v1 - a2 < 0 or a1[v1 - a2] < a1[v1]) and (v1 + a2 >= len(a1) or a1[v1 + a2] < a1[v1])))
