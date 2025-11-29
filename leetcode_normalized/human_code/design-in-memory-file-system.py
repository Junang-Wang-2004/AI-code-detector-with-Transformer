class C1(object):

    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ''

class C2(object):

    def __init__(self):
        self.__root = C1()

    def ls(self, a1):
        """
        """
        v1 = self.__getNode(a1)
        if v1.is_file:
            return [self.__split(a1, '/')[-1]]
        return sorted(v1.children.keys())

    def mkdir(self, a1):
        """
        """
        v1 = self.__putNode(a1)
        v1.is_file = False

    def addContentToFile(self, a1, a2):
        """
        """
        v1 = self.__putNode(a1)
        v1.is_file = True
        v1.content += a2

    def readContentFromFile(self, a1):
        """
        """
        return self.__getNode(a1).content

    def __getNode(self, a1):
        v1 = self.__root
        for v2 in self.__split(a1, '/'):
            v1 = v1.children[v2]
        return v1

    def __putNode(self, a1):
        v1 = self.__root
        for v2 in self.__split(a1, '/'):
            if v2 not in v1.children:
                v1.children[v2] = C1()
            v1 = v1.children[v2]
        return v1

    def __split(self, a1, a2):
        if a1 == '/':
            return []
        return a1.split('/')[1:]
