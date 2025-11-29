class C1(object):

    def maximumLength(self, a1):
        """
        """
        return max(sum((x % 2 == 0 for v1 in a1)), sum((v1 % 2 == 1 for v1 in a1)), sum((a1[i] % 2 != a1[i + 1] % 2 for v2 in range(len(a1) - 1))) + 1)
