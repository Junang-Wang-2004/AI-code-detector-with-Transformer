import collections

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__king = a1
        self.__family_tree = collections.defaultdict(list)
        self.__dead = set()

    def birth(self, a1, a2):
        """
        """
        self.__family_tree[a1].append(a2)

    def death(self, a1):
        """
        """
        self.__dead.add(a1)

    def getInheritanceOrder(self):
        """
        """
        v1 = []
        v2 = [self.__king]
        while v2:
            v3 = v2.pop()
            if v3 not in self.__dead:
                v1.append(v3)
            if v3 not in self.__family_tree:
                continue
            for v4 in reversed(self.__family_tree[v3]):
                v2.append(v4)
        return v1
