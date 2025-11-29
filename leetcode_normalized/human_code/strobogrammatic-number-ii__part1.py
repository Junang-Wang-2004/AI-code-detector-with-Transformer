class C1(object):

    def findStrobogrammatic(self, a1):
        """
        """
        v1 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        v2 = ['0', '1', '8'] if a1 % 2 else ['']
        for v3 in range(a1 % 2, a1, 2):
            v2 = [a + num + b for v4, v5 in v1.items() if v3 != a1 - 2 or v4 != '0' for v6 in v2]
        return v2
