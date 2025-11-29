class C1(object):

    def __init__(self, a1):
        """
        """
        self.__parent = a1
        self.__children = [[] for v1 in range(len(a1))]
        for v2, v3 in enumerate(a1):
            if v3 != -1:
                self.__children[v3].append(v2)
        self.__locked = {}

    def lock(self, a1, a2):
        """
        """
        if a1 in self.__locked:
            return False
        self.__locked[a1] = a2
        return True

    def unlock(self, a1, a2):
        """
        """
        if self.__locked.get(a1) != a2:
            return False
        del self.__locked[a1]
        return True

    def upgrade(self, a1, a2):
        """
        """
        v1 = a1
        while v1 != -1:
            if v1 in self.__locked:
                return False
            v1 = self.__parent[v1]
        v2 = False
        v3 = [a1]
        while v3:
            v1 = v3.pop()
            if v1 in self.__locked:
                del self.__locked[v1]
                v2 = True
            for v4 in self.__children[v1]:
                v3.append(v4)
        if v2:
            self.__locked[a1] = a2
        return v2
