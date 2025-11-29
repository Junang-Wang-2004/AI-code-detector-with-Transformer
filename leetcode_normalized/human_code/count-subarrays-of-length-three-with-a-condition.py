class C1(object):

    def countSubarrays(self, a1):
        """
        """
        return sum(((a1[i - 1] + a1[i + 1]) * 2 == a1[i] for v1 in range(1, len(a1) - 1)))
