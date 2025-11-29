class C1(object):

    def divideArray(self, a1, a2):
        """
        """
        a1.sort()
        return [a1[v1:v1 + 3] for v1 in range(0, len(a1), 3)] if all((a1[i + 2] - a1[i] <= a2 for v1 in range(0, len(a1), 3))) else []
