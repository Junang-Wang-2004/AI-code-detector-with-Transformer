class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def __init__(self):
        self.__memo = {1: [C1(0)]}

    def allPossibleFBT(self, a1):
        """
        """
        if a1 % 2 == 0:
            return []
        if a1 not in self.__memo:
            v1 = []
            for v2 in range(a1):
                for v3 in self.allPossibleFBT(v2):
                    for v4 in self.allPossibleFBT(a1 - 1 - v2):
                        v5 = C1(0)
                        v5.left = v3
                        v5.right = v4
                        v1.append(v5)
            self.__memo[a1] = v1
        return self.__memo[a1]
