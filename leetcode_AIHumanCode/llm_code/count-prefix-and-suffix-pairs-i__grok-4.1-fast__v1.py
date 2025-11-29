class Solution:
    def countPrefixSuffixPairs(self, words):
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.count = 0

        root = TrieNode()
        total = 0
        for s in words:
            current = root
            length = len(s)
            for pos in range(length):
                start_char = s[pos]
                end_char = s[length - 1 - pos]
                pair = (start_char, end_char)
                if pair not in current.children:
                    current.children[pair] = TrieNode()
                current = current.children[pair]
                total += current.count
            current.count += 1
        return total
