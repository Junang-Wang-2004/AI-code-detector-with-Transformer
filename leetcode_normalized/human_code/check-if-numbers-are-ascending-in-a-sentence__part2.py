class C1(object):

    def areNumbersAscending(self, a1):
        """
        """
        v1 = [int(x) for v2 in a1.split() if v2.isdigit()]
        return all((v1[i] < v1[i + 1] for v3 in range(len(v1) - 1)))
