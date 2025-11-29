class C1(object):

    def categorizeBox(self, a1, a2, a3, a4):
        """
        """
        v1 = any((x >= 10 ** 4 for v2 in (a1, a2, a3))) or a1 * a2 * a3 >= 10 ** 9
        v3 = a4 >= 100
        if v1 and v3:
            return 'Both'
        if v1:
            return 'Bulky'
        if v3:
            return 'Heavy'
        return 'Neither'
