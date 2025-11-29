class Solution:
    def countPrefixSuffixPairs(self, words):
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.val = 0

        head = TrieNode()
        total = 0
        for term in words:
            walker = head
            length = len(term)
            for step in range(length):
                front = term[step]
                back = term[length - 1 - step]
                edge = (front, back)
                if edge not in walker.children:
                    walker.children[edge] = TrieNode()
                walker = walker.children[edge]
                total += walker.val
            walker.val += 1
        return total
