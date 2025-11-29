class TrieNode:
    def __init__(self):
        self.children = {}
        self.pass_count = 0
        self.word_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        current.pass_count += 1
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
            current.pass_count += 1
        current.word_count += 1

    def countWordsEqualTo(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return 0
            current = current.children[ch]
        return current.word_count

    def countWordsStartingWith(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return 0
            current = current.children[ch]
        return current.pass_count

    def erase(self, word):
        if self.countWordsEqualTo(word) == 0:
            return
        current = self.root
        current.pass_count -= 1
        for ch in word:
            next_node = current.children[ch]
            if next_node.pass_count == 1:
                del current.children[ch]
                return
            current = next_node
            current.pass_count -= 1
        current.word_count -= 1
