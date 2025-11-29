class C1(object):

    def categorizeBox(self, a1, a2, a3, a4):
        """
        """
        v1 = ['Neither', 'Heavy', 'Bulky', 'Both']
        v2 = 2 * (any((x >= 10 ** 4 for v3 in (a1, a2, a3))) or a1 * a2 * a3 >= 10 ** 9) + int(a4 >= 100)
        return v1[v2]
