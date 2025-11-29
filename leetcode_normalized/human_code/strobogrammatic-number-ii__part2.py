class C1(object):

    def findStrobogrammatic(self, a1):
        """
        """
        v1 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        def findStrobogrammaticRecu(a1, a2):
            if a2 == 0:
                return ['']
            elif a2 == 1:
                return ['0', '1', '8']
            v1 = []
            for v2 in findStrobogrammaticRecu(a1, a2 - 2):
                for v3, v4 in v1.items():
                    if a1 != a2 or v3 != '0':
                        v1.append(v3 + v2 + v4)
            return v1
        return findStrobogrammaticRecu(a1, a1)
