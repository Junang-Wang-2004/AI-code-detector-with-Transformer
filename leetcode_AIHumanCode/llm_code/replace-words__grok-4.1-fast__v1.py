class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary, sentence):
        root = TrieNode()
        for term in dictionary:
            node = root
            for char in term:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

        def shorten(term):
            node = root
            result = []
            for char in term:
                if char not in node.children:
                    break
                node = node.children[char]
                result.append(char)
                if node.is_end:
                    return ''.join(result)
            return term

        parts = sentence.split()
        return ' '.join(shorten(part) for part in parts)
