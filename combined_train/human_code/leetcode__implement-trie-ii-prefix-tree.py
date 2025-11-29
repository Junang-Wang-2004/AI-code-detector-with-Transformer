class C1:

    def __init__(self):
        self.children = [None] * 26
        self.pcnt = 0
        self.cnt = 0

class C2(object):

    def __init__(self):
        self.__trie = C1()

    def insert(self, a1):
        """
        """
        v1 = self.__trie
        v1.pcnt += 1
        for v2 in a1:
            if v1.children[ord(v2) - ord('a')] is None:
                v1.children[ord(v2) - ord('a')] = C1()
            v1 = v1.children[ord(v2) - ord('a')]
            v1.pcnt += 1
        v1.cnt += 1

    def countWordsEqualTo(self, a1):
        """
        """
        v1 = self.__trie
        for v2 in a1:
            if v1.children[ord(v2) - ord('a')] is None:
                return 0
            v1 = v1.children[ord(v2) - ord('a')]
        return v1.cnt

    def countWordsStartingWith(self, a1):
        """
        """
        v1 = self.__trie
        for v2 in a1:
            if v1.children[ord(v2) - ord('a')] is None:
                return 0
            v1 = v1.children[ord(v2) - ord('a')]
        return v1.pcnt

    def erase(self, a1):
        """
        """
        v1 = self.countWordsEqualTo(a1)
        if not v1:
            return
        v2 = self.__trie
        v2.pcnt -= 1
        for v3 in a1:
            if v2.children[ord(v3) - ord('a')].pcnt == 1:
                v2.children[ord(v3) - ord('a')] = None
                return
            v2 = v2.children[ord(v3) - ord('a')]
            v2.pcnt -= 1
        v2.cnt -= 1
