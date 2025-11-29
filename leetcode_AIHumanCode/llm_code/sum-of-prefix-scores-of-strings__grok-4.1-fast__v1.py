class TrieNode:
    def __init__(self):
        self.children = {}
        self.pass_count = 0

class Solution:
    def sumPrefixScores(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.pass_count += 1
        
        scores = []
        for word in words:
            score = 0
            node = root
            for char in word:
                node = node.children[char]
                score += node.pass_count
            scores.append(score)
        return scores
