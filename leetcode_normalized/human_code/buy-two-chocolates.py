class C1(object):

    def buyChoco(self, a1, a2):
        """
        """
        v1 = min(range(len(a1)), key=lambda x: a1[x])
        v2 = min((v2 for v2 in range(len(a1)) if v2 != v1), key=lambda x: a1[x])
        return a2 - (a1[v1] + a1[v2]) if a1[v1] + a1[v2] <= a2 else a2
