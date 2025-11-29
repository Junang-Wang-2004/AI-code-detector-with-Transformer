class Node:
    def __init__(self):
        self.children = [None] * 26
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.word_end = True

    def search(self, word):
        final = self._walk(word)
        return final is not None and final.word_end

    def startsWith(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, text):
        curr = self.root
        for char in text:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return None
            curr = curr.children[index]
        return curr
